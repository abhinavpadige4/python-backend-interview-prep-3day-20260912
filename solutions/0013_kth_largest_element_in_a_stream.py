"""
LeetCode 703: Kth Largest Element in a Stream
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Problem:
Design a class to find the kth largest element in a stream. Note that it is the kth largest 
element in the sorted order, not the kth distinct element.

Implement KthLargest class:
- KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
- int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Solution Approach:
Use a min-heap of size k to store the k largest elements seen so far.
- The root of the heap will be the kth largest element
- When adding a new element, if it's larger than the root, replace the root and heapify
- This ensures we always have the k largest elements in the heap

Time Complexity: 
  - Initialization: O(n log k) where n is length of nums
  - Add operation: O(log k) for heap operations
Space Complexity: O(k) for storing the heap
"""

import heapq
from typing import List

class KthLargest:
    """
    Class to find the kth largest element in a stream using min-heap.
    """
    
    def __init__(self, k: int, nums: List[int]):
        """
        Initialize the data structure.
        
        Args:
            k: The kth largest element to find
            nums: Initial stream of integers
        """
        self.k = k
        self.heap = []
        
        # Add all initial numbers to heap
        for num in nums:
            self.add(num)
    
    def add(self, val: int) -> int:
        """
        Add a value to the stream and return the kth largest element.
        
        Args:
            val: Integer to add to the stream
            
        Returns:
            The kth largest element in the stream
        """
        # Push the new value to heap
        heapq.heappush(self.heap, val)
        
        # If heap size exceeds k, remove the smallest element
        if len(self.heap) > k:
            heapq.heappop(self.heap)
        
        # The root of the min-heap is the kth largest element
        return self.heap[0]

# Alternative implementation using sorting (less efficient but simpler to understand)
class KthLargestSorting:
    """
    Alternative implementation using sorting (for educational purposes).
    Less efficient but easier to understand.
    """
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)  # Keep sorted in descending order
    
    def add(self, val: int) -> int:
        # Insert val in sorted position
        import bisect
        bisect.insort(self.nums, val, lo=0, hi=len(self.nums), key=lambda x: -x)
        # Return kth largest (index k-1 in descending order)
        return self.nums[self.k - 1] if len(self.nums) >= self.k else None

# Alternative implementation using quickselect concepts (more complex)
class KthLargestOptimized:
    """
    Optimized version that avoids unnecessary heap operations.
    """
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums[:]
        heapq.heapify(self.heap)
        
        # Keep only the k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)
    
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        
        return self.heap[0]

# Test cases
if __name__ == "__main__":
    print("Testing KthLargest implementation:")
    print("=" * 40)
    
    # Test case 1 from LeetCode example
    k = 3
    arr = [4, 5, 8, 2]
    kth_largest = KthLargest(k, arr)
    
    print(f"Initialized with k={k}, nums={arr}")
    print(f"Initial heap state: {kth_largest.heap}")
    print()
    
    # Test add operations
    test_values = [3, 5, 10, 9, 4]
    expected_results = [4, 5, 5, 8, 8]  # Expected kth largest after each add
    
    for i, val in enumerate(test_values):
        result = kth_largest.add(val)
        print(f"Add {val}: kth largest = {result} (expected: {expected_results[i]}) {'✓' if result == expected_results[i] else '✗'}")
        print(f"  (f"Heap state: {kth_largest.heap}")
        print()
    
    # Test case 2: Starting with empty stream
    print("Test case 2: Empty initial stream")
    kth_largest2 = KthLargest(2, [])
    print(f"Initialized with k=2, nums=[]")
    print(f"Initial heap state: {kth_largest2.heap}")
    print()
    
    test_values2 = [3, 21, 324, 32, 321, 321, 321, 32, 324, 323, 324]
    expected_results2 = [None, 321, 321, 321, 321, 321, 321, 321, 323, 323]  # First one is None since we need 2 elements
    
    for i, val in enumerate(test_values2):
        result = kth_largest2.add(val)
        # Handle None case for first element
        expected = expected_results2[i] if i > 0 else None
        print(f"Add {val}: kth largest = {result} (expected: {expected}) {'✓' if result == expected else '✗'}")
        print(f"Heap state: {kth_largest2.heap}")
        print()
    
    # Test case 3: Large k value
    print("Test case 3: k larger than initial array")
    kth_largest3 = KthLargest(5, [1, 2, 3, 4])
    print(f"Initialized with k=5, nums=[1, 2, 3, 4]")
    print(f"Initial heap state: {kth_largest3.heap}")
    print()
    
    test_values3 = [5, 6, 7, 8, 9, 10]
    expected_results3 = [None, None, None, None, 4, 5]  # Need 5 elements before returning valid kth largest
    
    for i, val in enumerate(test_values3):
        result = kth_largest3.add(val)
        # For first 4 adds, we won't have k elements yet
        expected = expected_results3[i] if len(kth_largest3.heap) >= kth_largest3.k else None
        actual_expected = sorted(kth_largest3.heap, reverse=True)[kth_largest3.k - 1] if len(kth_largest3.heap) >= kth_largest3.k else None
        print(f"Add {val}: kth largest = {result} (heap size: {len(kth_largest3.heap)})")
        print(f"Heap state: {kth_largest3.heap}")
        print()
    
    print("Testing alternative implementations:")
    print("=" * 40)
    
    # Test sorting approach
    print("Sorting approach:")
    kth_largest_sort = KthLargestSorting(3, [4, 5, 8, 2])
    print(f"Add 3: {kth_largest_sort.add(3)}")  # Should be 4
    print(f"Add 5: {kth_largest_sort.add(5)}")  # Should be 5
    print(f"Add 10: {kth_largest_sort.add(10)}")  # Should be 5
    print()
    
    # Test optimized approach
    print("Optimized approach:")
    kth_largest_opt = KthLargestOptimized(3, [4, 5, 8, 2])
    print(f"Add 3: {kth_largest_opt.add(3)}")  # Should be 4
    print(f"Add 5: {kth_largest_opt.add(5)}")  # Should be 5
    print(f"Add 10: {kth_largest_opt.add(10)}")  # Should be 5