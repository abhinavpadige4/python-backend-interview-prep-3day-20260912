"""
LeetCode 380: Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/

Problem:
Implement the RandomizedSet class:
- RandomizedSet() Initializes the RandomizedSet object.
- bool insert(int val) Inserts an item val into the set if not present. 
  Returns true if the item was not present, false otherwise.
- bool remove(int val) Removes an item val from the set if present. 
  Returns true if the item was present, false otherwise.
- int getRandom() Returns a random element from the current set of elements 
  (it's guaranteed that at least one element exists when this method is called).
  Each element must have the same probability of being returned.

Solution Approach:
Use a combination of list and dictionary:
- List to store elements for O(1) random access
- Dictionary to map values to their indices in the list for O(1) lookup
- For removal: swap element with last element, pop from end, update dictionary

Time Complexity: O(1) average for all operations
Space Complexity: O(n) where n is the number of elements in the set
"""

import random
from typing import Dict, List

class RandomizedSet:
    """
    RandomizedSet that supports insert, remove, and getRandom in O(1) time.
    """
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums_list: List[int] = []  # Store elements for random access
        self.val_to_index: Dict[int, int] = {}  # Map value to its index in list
    
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        
        Args:
            val: Value to insert
            
        Returns:
            True if value was inserted, False if it already existed
        """
        if val in self.val_to_index:
            return False
        
        # Add to end of list
        self.nums_list.append(val)
        # Map value to its index
        self.val_to_index[val] = len(self.nums_list) - 1
        return True
    
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        
        Args:
            val: Value to remove
            
        Returns:
            True if value was removed, False if it didn't exist
        """
        if val not in self.val_to_index:
            return False
        
        # Get index of element to remove
        index_to_remove = self.val_to_index[val]
        # Get last element in list
        last_element = self.nums_list[-1]
        
        # Move last element to the position of element to remove
        self.nums_list[index_to_remove] = last_element
        # Update the index of last element in dictionary
        self.val_to_index[last_element] = index_to_remove
        
        # Remove last element from list
        self.nums_list.pop()
        # Remove the value from dictionary
        del self.val_to_index[val]
        
        return True
    
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        
        Returns:
            Random element from the set
        """
        return random.choice(self.nums_list)

# Alternative implementation using try/except for cleaner code
class RandomizedSetAlternative:
    """
    Alternative implementation with slightly different approach.
    """
    
    def __init__(self):
        self.nums = []
        self.pos = {}
    
    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.nums.append(val)
        self.pos[val] = len(self.nums) - 1
        return True
    
    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        idx = self.pos[val]
        last = self.nums[-1]
        self.nums[idx] = last
        self.pos[last] = idx
        self.nums.pop()
        del self.pos[val]
        return True
    
    def getRandom(self) -> int:
        return random.choice(self.nums)

# Test cases
if __name__ == "__main__":
    # Test case 1
    print("Test Case 1:")
    randomized_set = RandomizedSet()
    print(f"Insert 1: {randomized_set.insert(1)}")  # Returns True
    print(f"Remove 2: {randomized_set.remove(2)}")  # Returns False
    print(f"Insert 2: {randomized_set.insert(2)}")  # Returns True
    print(f"Get Random: {randomized_set.getRandom()}")  # Returns 1 or 2 randomly
    print(f"Remove 1: {randomized_set.remove(1)}")  # Returns True
    print(f"Insert 2: {randomized_set.insert(2)}")  # Returns False (already present)
    print(f"Get Random: {randomized_set.getRandom()}")  # Returns 2
    print()
    
    # Test case 2 - Multiple insertions and removals
    print("Test Case 2:")
    randomized_set2 = RandomizedSet()
    operations = [
        ("insert", 1),
        ("insert", 2),
        ("insert", 3),
        ("insert", 4),
        ("getRandom", None),
        ("remove", 2),
        ("insert", 5),
        ("getRandom", None),
        ("remove", 1),
        ("getRandom", None)
    ]
    
    for op, val in operations:
        if op == "insert":
            result = randomized_set2.insert(val)
            print(f"Insert {val}: {result}")
        elif op == "remove":
            result = randomized_set2.remove(val)
            print(f"Remove {val}: {result}")
        elif op == "getRandom":
            result = randomized_set2.getRandom()
            print(f"Get Random: {result}")
    print()
    
    # Test case 3 - Edge cases
    print("Test Case 3 (Edge Cases):")
    randomized_set3 = RandomizedSet()
    print(f"Insert 0: {randomized_set3.insert(0)}")  # True
    print(f"Remove 0: {randomized_set3.remove(0)}")  # True
    print(f"Remove 0: {randomized_set3.remove(0)}")  # False (already removed)
    print(f"Insert -1: {randomized_set3.insert(-1)}")  # True
    print(f"Get Random: {randomized_set3.getRandom()}")  # -1