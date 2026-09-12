"""
LeetCode 136: Single Number
https://leetcode.com/problems/single-number/

Problem:
Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.

Solution Approach:
Use XOR operation. XOR of a number with itself is 0, and XOR of a number with 0 is the number itself.
So, XOR-ing all numbers will cancel out the pairs and leave the single number.

Time Complexity: O(n) - we iterate through the array once
Space Complexity: O(1) - we use only a single variable
"""

from typing import List

def single_number(nums: List[int]) -> int:
    """
    Find the element that appears only once in the array.
    
    Args:
        nums: List of integers where every element appears twice except one
        
    Returns:
        The integer that appears only once
    """
    result = 0
    for num in nums:
        result ^= num
    return result

# Alternative solution using hashmap (less optimal)
def single_number_hashmap(nums: List[int]) -> int:
    """
    Alternative solution using hashmap to count frequencies.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    for num, count in freq.items():
        if count == 1:
            return num
    return -1

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 2, 1]
    print(f"Input: {nums1}")
    print(f"Single Number: {single_number(nums1)}")  # Expected: 1
    
    # Test case 2
    nums2 = [4, 1, 2, 1, 2]
    print(f"Input: {nums2}")
    print(f"Single Number: {single_number(nums2)}")  # Expected: 4
    
    # Test case 3
    nums3 = [1]
    print(f"Input: {nums3}")
    print(f"Single Number: {single_number(nums3)}")  # Expected: 1