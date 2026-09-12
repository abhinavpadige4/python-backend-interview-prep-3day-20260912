"""
LeetCode 202: Happy Number
https://leetcode.com/problems/happy-number/

Problem:
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Solution Approach:
Use a set to detect cycles. If we see a number again, we know we're in a cycle and it's not a happy number.
Otherwise, continue the process until we reach 1.

Time Complexity: O(log n) per iteration, but the number of iterations is bounded due to cycle detection
Space Complexity: O(log n) for storing seen numbers
"""

def is_happy(n: int) -> bool:
    """
    Determine if a number is happy.
    
    Args:
        n: Positive integer to check
        
    Returns:
        True if n is a happy number, False otherwise
    """
    seen = set()
    
    while n != 1 and n not in seen:
        seen.add(n)
        # Calculate sum of squares of digits
        n = sum(int(digit) ** 2 for digit in str(n))
    
    return n == 1

def get_next_number(n: int) -> int:
    """
    Helper function to calculate the next number in the sequence.
    
    Args:
        n: Current number
        
    Returns:
        Sum of squares of digits of n
    """
    total_sum = 0
    while n > 0:
        digit = n % 10
        total_sum += digit ** 2
        n //= 10
    return total_sum

def is_happy_optimized(n: int) -> bool:
    """
    Optimized version using mathematical approach for digit extraction.
    
    Time Complexity: O(log n) per iteration
    Space Complexity: O(log n)
    """
    seen = set()
    
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next_number(n)
    
    return n == 1

# Test cases
if __name__ == "__main__":
    # Test case 1
    n1 = 19
    print(f"Input: {n1}")
    print(f"Is Happy: {is_happy(n1)}")  # Expected: True
    print(f"Is Happy (Optimized): {is_happy_optimized(n1)}")
    
    # Test case 2
    n2 = 2
    print(f"Input: {n2}")
    print(f"Is Happy: {is_happy(n2)}")  # Expected: False
    print(f"Is Happy (Optimized): {is_happy_optimized(n2)}")
    
    # Test case 3
    n3 = 1
    print(f"Input: {n3}")
    print(f"Is Happy: {is_happy(n3)}")  # Expected: True
    print(f"Is Happy (Optimized): {is_happy_optimized(n3)}")