"""
LeetCode 704: Binary Search
https://leetcode.com/problems/binary-search/

Problem:
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. 
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Solution Approach:
Use binary search algorithm. Repeatedly divide the search interval in half.
If the value of the search key is less than the item in the middle of the interval,
narrow the interval to the lower half. Otherwise narrow it to the upper half.
Repeatedly check until the value is found or the interval is empty.

Time Complexity: O(log n) - we halve the search space each iteration
Space Complexity: O(1) - we use only constant extra space
"""

from typing import List

def search(nums: List[int], target: int) -> int:
    """
    Search for target in sorted array using binary search.
    
    Args:
        nums: Sorted list of integers in ascending order
        target: Integer to search for
        
    Returns:
        Index of target if found, otherwise -1
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Prevents potential overflow
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def search_recursive(nums: List[int], target: int) -> int:
    """
    Recursive version of binary search.
    
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion stack
    """
    def binary_search(left: int, right: int) -> int:
        if left > right:
            return -1
        
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return binary_search(mid + 1, right)
        else:
            return binary_search(left, mid - 1)
    
    return binary_search(0, len(nums) - 1)

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Search Result: {search(nums1, target1)}")  # Expected: 4
    print(f"Search Recursive: {search_recursive(nums1, target1)}")
    
    # Test case 2
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Search Result: {search(nums2, target2)}")  # Expected: -1
    print(f"Search Recursive: {search_recursive(nums2, target2)}")
    
    # Test case 3
    nums3 = [5]
    target3 = 5
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Search Result: {search(nums3, target3)}")  # Expected: 0
    print(f"Search Recursive: {search_recursive(nums3, target3)}")
    
    # Test case 4
    nums4 = []
    target4 = 5
    print(f"Input: nums = {nums4}, target = {target4}")
    print(f"Search Result: {search(nums4, target4)}")  # Expected: -1