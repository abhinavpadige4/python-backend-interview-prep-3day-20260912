"""
LeetCode 535: Encode and Decode TinyURL
https://leetcode.com/problems/encode-and-decode-tinyurl/

Problem:
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl 
and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service.
There is no restriction on how your encode/decode algorithm should work.
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Solution Approach:
Use a hashmap (dictionary) to store mappings between original URLs and their short codes.
Generate random short codes for each URL and store the mapping.
For decoding, look up the short code in the hashmap to get the original URL.

Time Complexity: O(1) average for both encode and decode operations
Space Complexity: O(n) where n is the number of URLs stored
"""

import random
import string
from typing import Dict

class Codec:
    """
    Codec for encoding and decoding URLs using hashmap storage.
    """
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Two-way mapping for efficiency
        self.url_to_code: Dict[str, str] = {}   # original URL -> short code
        self.code_to_url: Dict[str, str] = {}   # short code -> original URL
        self.chars = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
        self.base_url = "http://tinyurl.com/"
    
    def encode(self, longUrl: str) -> str:
        """
        Encodes a URL to a shortened URL.
        
        Args:
            longUrl: Original URL to encode
            
        Returns:
            Shortened URL
        """
        # If URL already encoded, return existing short URL
        if longUrl in self.url_to_code:
            return self.base_url + self.url_to_code[longUrl]
        
        # Generate a unique short code
        while True:
            short_code = ''.join(random.choices(self.chars, k=6))  # 6-character code
            if short_code not in self.code_to_url:
                break
        
        # Store the mapping
        self.url_to_code[longUrl] = short_code
        self.code_to_url[short_code] = longUrl
        
        return self.base_url + short_code
    
    def decode(self, shortUrl: str) -> str:
        """
        Decodes a shortened URL to its original URL.
        
        Args:
            shortUrl: Shortened URL to decode
            
        Returns:
            Original URL
        """
        # Extract the short code from the URL
        short_code = shortUrl.replace(self.base_url, "")
        
        # Return the original URL if found, otherwise return empty string
        return self.code_to_url.get(short_code, "")

# Alternative implementation using incremental IDs
class CodecIncremental:
    """
    Alternative implementation using incremental IDs instead of random strings.
    """
    
    def __init__(self):
        self.url_to_id: Dict[str, int] = {}
        self.id_to_url: Dict[int, str] = {}
        self.next_id = 1
        self.base_url = "http://tinyurl.com/"
    
    def encode(self, longUrl: str) -> str:
        if longUrl in self.url_to_id:
            return self.base_url + str(self.url_to_id[longUrl])
        
        # Assign new ID
        current_id = self.next_id
        self.url_to_id[longUrl] = current_id
        self.id_to_url[current_id] = longUrl
        self.next_id += 1
        
        return self.base_url + str(current_id)
    
    def decode(self, shortUrl: str) -> str:
        try:
            url_id = int(shortUrl.replace(self.base_url, ""))
            return self.id_to_url.get(url_id, "")
        except ValueError:
            return ""

# Alternative implementation using hash-based approach (consistent encoding)
class CodecHash:
    """
    Alternative implementation using hash-based encoding for consistency.
    Same URL always encodes to same short URL.
    """
    
    def __init__(self):
        self.code_to_url: Dict[str, str] = {}
        self.base_url = "http://tinyurl.com/"
        # Using a larger character set for shorter codes
        self.chars = string.ascii_letters + string.digits
    
    def _hash_string(self, s: str) -> str:
        """
        Simple hash function to convert string to index.
        In practice, you'd use a proper hash like SHA-256 and take first few chars.
        """
        hash_value = 0
        for char in s:
            hash_value = (hash_value * 31 + ord(char)) % (10**8)
        # Convert to base62 string
        result = ""
        if hash_value == 0:
            return self.chars[0]
        while hash_value > 0:
            result = self.chars[hash_value % 62] + result
            hash_value //= 62
        # Pad to ensure minimum length
        return result.rjust(6, self.chars[0])
    
    def encode(self, longUrl: str) -> str:
        # Generate consistent hash-based code
        short_code = self._hash_string(longUrl)
        
        # Handle collisions (rare with good hash function)
        original_code = short_code
        counter = 0
        while short_code in self.code_to_url and self.code_to_url[short_code] != longUrl:
            # Collision detected, modify the code
            short_code = self._hash_string(longUrl + str(counter))
            counter += 1
            # Prevent infinite loop in case of hash function issues
            if counter > 1000:
                # Fallback to random approach
                import random
                short_code = ''.join(random.choices(self.chars, k=6))
                break
        
        # Store mapping
        self.code_to_url[short_code] = longUrl
        return self.base_url + short_code
    
    def decode(self, shortUrl: str) -> str:
        short_code = shortUrl.replace(self.base_url, "")
        return self.code_to_url.get(short_code, "")

# Test cases
if __name__ == "__main__":
    print("Testing Codec implementation:")
    print("=" * 40)
    
    codec = Codec()
    
    # Test case 1: Basic encode/decode
    url1 = "https://leetcode.com/problems/design-tinyurl"
    encoded1 = codec.encode(url1)
    decoded1 = codec.decode(encoded1)
    
    print(f"Original URL: {url1}")
    print(f"Encoded URL:  {encoded1}")
    print(f"Decoded URL:  {decoded1}")
    print(f"Match: {url1 == decoded1}")
    print()
    
    # Test case 2: Same URL should return same encoding
    encoded1_again = codec.encode(url1)
    print(f"Second encoding: {encoded1_again}")
    print(f"Same encoding: {encoded1 == encoded1_again}")
    print()
    
    # Test case 3: Different URLs
    url2 = "https://www.example.com/very/long/url/path/here"
    encoded2 = codec.encode(url2)
    decoded2 = codec.decode(encoded2)
    
    print(f"Original URL: {url2}")
    print(f"Encoded URL:  {encoded2}")
    print(f"Decoded URL:  {decoded2}")
    print(f"Match: {url2 == decoded2}")
    print()
    
    # Test case 4: Empty and edge case URLs
    url3 = ""
    encoded3 = codec.encode(url3)
    decoded3 = codec.decode(encoded3)
    
    print(f"Original URL: '{url3}'")
    print(f"Encoded URL:  '{encoded3}'")
    print(f"Decoded URL:  '{decoded3}'")
    print(f"Match: {url3 == decoded3}")
    print()
    
    # Test case 5: Multiple URLs
    urls = [
        "https://google.com",
        "https://github.com/user/repo",
        "https://stackoverflow.com/questions/123456",
        "http://localhost:8080/api/users"
    ]
    
    print("Testing multiple URLs:")
    for i, url in enumerate(urls):
        encoded = codec.encode(url)
        decoded = codec.decode(encoded)
        match = url == decoded
        print(f"URL {i+1}: {'✓' if match else '✗'} {url}")
        if not match:
            print(f"  Encoded: {encoded}")
            print(f"  Decoded: {decoded}")
    print()
    
    print("Testing Incremental ID approach:")
    print("=" * 40)
    codec_inc = CodecIncremental()
    
    url_test = "https://leetcode.com/problems/design-tinyurl"
    encoded_inc = codec_inc.encode(url_test)
    decoded_inc = codec_inc.decode(encoded_inc)
    
    print(f"Original URL: {url_test}")
    print(f"Encoded URL:  {encoded_inc}")
    print(f"Decoded URL:  {decoded_inc}")
    print(f"Match: {url_test == decoded_inc}")