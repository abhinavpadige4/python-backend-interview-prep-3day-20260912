"""
LeetCode 1114: Print in Order
https://leetcode.com/problems/print-in-order/

Problem:
Suppose we have a class:
  public class Foo {
    public void first() { print("first"); }
    public void second() { print("second"); }
    public void third() { print("third"); }
  }
The same instance of Foo will be passed to three different threads:
  Thread A: calls first()
  Thread B: calls second()
  Thread C: calls third()
Design a mechanism to ensure that:
  second() is executed after first()
  third() is executed after second()

Solution Approach:
Use threading synchronization primitives (Locks or Semaphores) to control execution order.
- Initialize locks such that second and third threads are blocked initially
- When first() completes, it releases the lock for second()
- When second() completes, it releases the lock for third()

Time Complexity: O(1) for each method call (constant time operations)
Space Complexity: O(1) - we use only fixed number of locks
"""

import threading
from typing import Callable

class Foo:
    """
    Class to ensure ordered execution of three methods using threading locks.
    """
    
    def __init__(self):
        """
        Initialize two locks. Initially lock second and third methods.
        """
        self.lock_first = threading.Lock()
        self.lock_second = threading.Lock()
        self.lock_third = threading.Lock()
        
        # Initially lock second and third (first can run immediately)
        self.lock_second.acquire()
        self.lock_third.acquire()
    
    def first(self, printFirst: Callable[[], None]) -> None:
        """
        Execute first() and allow second() to run.
        
        Args:
            printFirst: function to output "first"
        """
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        # Release lock for second()
        self.lock_second.release()
    
    def second(self, printSecond: Callable[[], None]) -> None:
        """
        Execute second() after first() completes and allow third() to run.
        
        Args:
            printSecond: function to output "second"
        """
        # Wait for first() to complete
        self.lock_second.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        # Release lock for third()
        self.lock_third.release()
    
    def third(self, printThird: Callable[[], None]) -> None:
        """
        Execute third() after second() completes.
        
        Args:
            printThird: function to output "third"
        """
        # Wait for second() to complete
        self.lock_third.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()

# Alternative implementation using Semaphores
class FooSemaphore:
    """
    Alternative implementation using Semaphores.
    """
    
    def __init__(self):
        # Semaphores initialized to 0 (blocked) except first which is 1 (allowed)
        self.sem_first = threading.Semaphore(1)
        self.sem_second = threading.Semaphore(0)
        self.sem_third = threading.Semaphore(0)
    
    def first(self, printFirst: Callable[[], None]) -> None:
        self.sem_first.acquire()
        printFirst()
        self.sem_second.release()
    
    def second(self, printSecond: Callable[[], None]) -> None:
        self.sem_second.acquire()
        printSecond()
        self.sem_third.release()
    
    def third(self, printThird: Callable[[], None]) -> None:
        self.sem_third.acquire()
        printThird()

# Alternative implementation using Barrier-like approach with Conditions
class FooCondition:
    """
    Alternative implementation using Condition variables.
    """
    
    def __init__(self):
        self.condition = threading.Condition()
        self.state = 1  # 1: first can run, 2: second can run, 3: third can run
    
    def first(self, printFirst: Callable[[], None]) -> None:
        with self.condition:
            # Wait for our turn (state == 1)
            while self.state != 1:
                self.condition.wait()
            printFirst()
            self.state = 2
            self.condition.notify_all()
    
    def second(self, printSecond: Callable[[], None]) -> None:
        with self.condition:
            # Wait for our turn (state == 2)
            while self.state != 2:
                self.condition.wait()
            printSecond()
            self.state = 3
            self.condition.notify_all()
    
    def third(self, printThird: Callable[[], None]) -> None:
        with self.condition:
            # Wait for our turn (state == 3)
            while self.state != 3:
                self.condition.wait()
            printThird()
            self.state = 1  # Reset for potential reuse
            self.condition.notify_all()

# Helper functions for testing
def print_first():
    print("first", end="")

def print_second():
    print("second", end="")

def print_third():
    print("third", end="")

# Test cases
if __name__ == "__main__":
    import time
    
    print("Testing Foo implementation with locks:")
    print("=" * 40)
    
    # Test 1: Basic functionality
    foo = Foo()
    
    # Create threads that will call the methods in arbitrary order
    def call_first():
        foo.first(print_first)
    
    def call_second():
        foo.second(print_second)
    
    def call_third():
        foo.third(print_third)
    
    # Start all threads simultaneously
    thread_a = threading.Thread(target=call_first)
    thread_b = threading.Thread(target=call_second)
    thread_c = threading.Thread(target=call_third)
    
    thread_a.start()
    thread_b.start()
    thread_c.start()
    
    # Wait for all threads to complete
    thread_a.join()
    thread_b.join()
    thread_c.join()
    
    print()  # New line after output
    print("Expected output: firstsecondthird")
    print()
    
    # Test 2: Different order of thread starts
    print("Testing with different thread start order:")
    foo2 = Foo()
    
    # Start threads in different order
    thread_c2 = threading.Thread(target=call_third)
    thread_a2 = threading.Thread(target=call_first)
    thread_b2 = threading.Thread(target=call_second)
    
    thread_c2.start()  # Start third first (should wait)
    time.sleep(0.1)    # Small delay
    thread_a2.start()  # Start first
    time.sleep(0.1)    # Small delay
    thread_b2.start()  # Start second
    
    thread_c2.join()
    thread_a2.join()
    thread_b2.join()
    
    print()  # New line after output
    print("Expected output: firstsecondthird")
    print()
    
    print("Testing Semaphore implementation:")
    print("=" * 40)
    foo_sem = FooSemaphore()
    
    thread_a_s = threading.Thread(target=lambda: foo_sem.first(print_first))
    thread_b_s = threading.Thread(target=lambda: foo_sem.second(print_second))
    thread_c_s = threading.Thread(target=lambda: foo_sem.third(print_third))
    
    thread_a_s.start()
    thread_b_s.start()
    thread_c_s.start()
    
    thread_a_s.join()
    thread_b_s.join()
    thread_c_s.join()
    
    print()  # New line after output
    print("Expected output: firstsecondthird")