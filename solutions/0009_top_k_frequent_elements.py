"""
LeetCode 347: Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Problem:
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Solution Approach:
1. Count frequencies of each element using Counter
2. Use a min-heap of size k to keep track of top k frequent elements
3. Alternative: Use bucket sort (frequency as index) for O(n) solution

Time Complexity: O(n log k) for heap approach, O(n) for bucket sort
Space Complexity: O(n) for storing frequencies and result
"""

from typing import List
from collections import Counter
import heapq

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Find the k most frequent elements using min-heap.
    
    Args:
        nums: List of integers
        k: Number of top frequent elements to return
        
    Returns:
        List of k most frequent elements
    """
    # Count frequencies
    freq_map = Counter(nums)
    
    # Use min-heap to keep track of top k elements
    # We store (-frequency, element) to simulate max-heap behavior
    # Actually, we'll use min-heap on frequency and keep size k
    min_heap = []
    
    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num))
        # If heap size exceeds k, remove the smallest frequency element
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    # Extract elements from heap
    return [num for freq, num in min_heap]

def top_k_frequent_bucket_sort(nums: List[int], k: int) -> List[int]:
    """
    Find the k most frequent elements using bucket sort.
    
    Time Complexity: O(n) - single pass to count, single pass to bucket, single pass to collect
    Space Complexity: O(n) - for frequency map and buckets
    """
    # Count frequencies
    freq_map = Counter(nums)
    
    # Create buckets where index = frequency
    # Maximum frequency can be len(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    
    # Place elements in buckets based on frequency
    for num, freq in freq_map.items():
        buckets[freq].append(num)
    
    # Collect results from highest frequency buckets
    result = []
    for freq in range(len(buckets) - 1, 0, -1):  # From high to low frequency
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    
    return result

def top_k_frequent_sorting(nums: List[int], k: int) -> List[int]:
    """
    Alternative solution using sorting.
    
    Time Complexity: O(n log n) for sorting
    Space Complexity: O(n) for frequency map
    """
    freq_map = Counter(nums)
    # Sort by frequency (descending) and take top k
    return [num for num, _ in sorted(freq_map.items(), key=lambda x: x[1], reverse=True)[:k]]

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Top K Frequent (Heap): {top_k_frequent(nums1, k1)}")  # Expected: [1, 2]
    print(f"Top K Frequent (Bucket): {top_k_frequent_bucket_sort(nums1, k1)}")
    print(f"Top K Frequent (Sorting): {top_k_frequent_sorting(nums1, k1)}")
    print()
    
    # Test case 2
    nums2 = [1]
    k2 = 1
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Top K Frequent (Heap): {top_k_frequent(nums2, k2)}")  # Expected: [1]
    print(f"Top K Frequent (Bucket): {top_k_frequent_bucket_sort(nums2, k2)}")
    print(f"Top K Frequent (Sorting): {top_k_frequent_sorting(nums2, k2)}")
    print()
    
    # Test case 3
    nums3 = [4, 1, -1, 2, -1, 2, 3]
    k3 = 2
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Top K Frequent (Heap): {top_k_frequent(nums3, k3)}")  # Expected: [-1, 2] or [2, -1]
    print(f"Top K Frequent (Bucket): {top_k_frequent_bucket_sort(nums3, k3)}")
    print(f"Top K Frequent (Sorting): {top_k_frequent_sorting(nums3, k3)}")
    print()
    
    # Test case 4 - k equals number of unique elements
    nums4 = [1, 2, 3, 4, 5]
    k4 = 5
    print(f"Input: nums = {nums4}, k = {k4}")
    print(f"Top K Frequent (Heap): {top_k_frequent(nums4, k4)}")  # Expected: [1, 2, 3, 4, 5] in any order
    print(f"Top K Frequent (Bucket): {top_k_frequent_bucket_sort(nums4, k4)}")