"""
LeetCode 242: Valid Anagram
https://leetcode.com/problems/valid-anagram/

Problem:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Solution Approach:
Count character frequencies in both strings and compare. If frequencies match, they are anagrams.

Time Complexity: O(n) where n is the length of the strings
Space Complexity: O(1) since we only store counts for 26 lowercase English letters
"""

from typing import Dict
from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    """
    Check if t is an anagram of s.
    
    Args:
        s: First string
        t: Second string
        
    Returns:
        True if t is an anagram of s, False otherwise
    """
    # If lengths differ, they can't be anagrams
    if len(s) != len(t):
        return False
    
    # Count characters in both strings
    return Counter(s) == Counter(t)

def is_anagram_array(s: str, t: str) -> bool:
    """
    Alternative solution using fixed-size array for character counts.
    Assumes input contains only lowercase English letters.
    
    Time Complexity: O(n)
    Space Complexity: O(1) - fixed size array of 26
    """
    if len(s) != len(t):
        return False
    
    # Array to store character frequencies (for 'a' to 'z')
    count = [0] * 26
    
    # Increment for s, decrement for t
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    
    # Check if all counts are zero
    return all(c == 0 for c in count)

def is_anagram_sorting(s: str, t: str) -> bool:
    """
    Alternative solution using sorting.
    
    Time Complexity: O(n log n) for sorting
    Space Complexity: O(n) for sorting space
    """
    return sorted(s) == sorted(t)

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "anagram"
    t1 = "nagaram"
    print(f"Input: s = '{s1}', t = '{t1}'")
    print(f"Is Anagram: {is_anagram(s1, t1)}")  # Expected: True
    print(f"Is Anagram (Array): {is_anagram_array(s1, t1)}")
    print(f"Is Anagram (Sorting): {is_anagram_sorting(s1, t1)}")
    
    # Test case 2
    s2 = "rat"
    t2 = "car"
    print(f"Input: s = '{s2}', t = '{t2}'")
    print(f"Is Anagram: {is_anagram(s2, t2)}")  # Expected: False
    print(f"Is Anagram (Array): {is_anagram_array(s2, t2)}")
    print(f"Is Anagram (Sorting): {is_anagram_sorting(s2, t2)}")
    
    # Test case 3
    s3 = ""
    t3 = ""
    print(f"Input: s = '{s3}', t = '{t3}'")
    print(f"Is Anagram: {is_anagram(s3, t3)}")  # Expected: True
    print(f"Is Anagram (Array): {is_anagram_array(s3, t3)}")