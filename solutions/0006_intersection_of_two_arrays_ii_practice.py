"""
LeetCode 350: Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Problem:
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays 
and you may return the result in any order.

This is the same problem as 349, for practice purposes.

Solution Approach:
Use a hashmap to count frequencies of elements in the smaller array for optimization, 
then iterate through the larger array and add elements to result if they exist 
in the hashmap with positive count.

Time Complexity: O(n + m) where n and m are lengths of nums1 and nums2
Space Complexity: O(min(n, m)) for the hashmap
"""

from typing import List
from collections import Counter

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Find intersection of two arrays with proper frequency handling.
    Optimized to use the smaller array for the hashmap.
    
    Args:
        nums1: First integer array
        nums2: Second integer array
        
    Returns:
        List containing intersection with proper frequencies
    """
    # Ensure nums1 is the smaller array for space optimization
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    # Count frequencies of elements in the smaller array
    freq = Counter(nums1)
    result = []
    
    # Iterate through the larger array and add to result if available in freq
    for num in nums2:
        if freq[num] > 0:
            result.append(num)
            freq[num] -= 1
    
    return result

def intersect_two_pointers(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Alternative solution using sorting and two pointers.
    
    Time Complexity: O(n log n + m log m) for sorting
    Space Complexity: O(1) or O(log n + m) for sorting space
    """
    nums1.sort()
    nums2.sort()
    
    i, j = 0, 0
    result = []
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            result.append(nums1[i])
            i += 1
            j += 1
    
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1_1 = [1, 2, 2, 1]
    nums2_1 = [2, 2]
    print(f"Input: nums1 = {nums1_1}, nums2 = {nums2_1}")
    print(f"Intersection: {intersect(nums1_1, nums2_1)}")  # Expected: [2, 2]
    print(f"Intersection (Two Pointers): {intersect_two_pointers(nums1_1, nums2_1)}")
    
    # Test case 2
    nums1_2 = [4, 9, 5]
    nums2_2 = [9, 4, 9, 8, 4]
    print(f"Input: nums1 = {nums1_2}, nums2 = {nums2_2}")
    print(f"Intersection: {intersect(nums1_2, nums2_2)}")  # Expected: [4, 9] or [9, 4]
    print(f"Intersection (Two Pointers): {intersect_two_pointers(nums1_2, nums2_2)}")
    
    # Test case 3 - Edge case: empty array
    nums1_3 = []
    nums2_3 = [1, 2, 3]
    print(f"Input: nums1 = {nums1_3}, nums2 = {nums2_3}")
    print(f"Intersection: {intersect(nums1_3, nums2_3)}")  # Expected: []
    print(f"Intersection (Two Pointers): {intersect_two_pointers(nums1_3, nums2_3)}")
    
    # Test case 4 - No intersection
    nums1_4 = [1, 2, 3]
    nums2_4 = [4, 5, 6]
    print(f"Input: nums1 = {nums1_4}, nums2 = {nums2_4}")
    print(f"Intersection: {intersect(nums1_4, nums2_4)}")  # Expected: []
    print(f"Intersection (Two Pointers): {intersect_two_pointers(nums1_4, nums2_4)}")