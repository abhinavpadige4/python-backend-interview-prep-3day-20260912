# Python Backend Interview Preparation - 3 Day Plan

This repository contains solutions to practice problems for a 3-day Python backend interview preparation plan.

## Day 1: Python Fundamentals, OOP, Data Structures, Algorithms, Backend Basics
- [x] Problem 136: Single Number
- [x] Problem 202: Happy Number
- [x] Problem 349: Intersection of Two Arrays II
- [x] Problem 242: Valid Anagram
- [x] Problem 704: Binary Search
- [x] Problem 350: Intersection of Two Arrays II (practice)

## Day 2: Databases, NoSQL, API Design, Concurrency
- [x] Problem 175: Combine Two Tables
- [x] Problem 176: Second Highest Salary
- [x] Problem 347: Top K Frequent Elements
- [x] Problem 380: Insert Delete GetRandom O(1)
- [x] Problem 1114: Print in Order

## Day 3: System Design, Testing, Final Review
- [x] Problem 535: Encode and Decode TinyURL
- [x] Problem 703: Kth Largest Element in a Stream

## Solutions Structure
Each solution is implemented in Python with:
- Clean, readable code
- Time and space complexity analysis
- Comments explaining the approach
- References to LeetCode problems

## How to Use
1. Each problem solution is in the `solutions/` directory
2. Files are named as `{problem_number}_{problem_name_in_snake_case}.py`
3. Run any solution with: `python solutions/{file_name}.py`

## Concepts Covered
- **Object-Oriented Programming (OOP)**: Classes, encapsulation, design patterns
- **Data Structures**: Arrays, HashMaps, Sets, Lists, Heaps, Trees
- **Algorithms**: Binary Search, Sorting, Hash-based solutions, Greedy approaches
- **Database Concepts**: SQL joins, aggregation, normalization
- **API Design**: REST principles, URL shortening services
- **Concurrency**: threading, synchronization, locks, semaphores
- **System Design Basics**: Caching, load balancing, scalability concepts
- **Testing Fundamentals**: Unit testing principles
- **Stream Processing**: Heap-based algorithms for real-time data

## Files Created
```
solutions/
├── 0001_single_number.py
├── 0002_happy_number.py
├── 0003_intersection_of_two_arrays_ii.py
├── 0004_valid_anagram.py
├── 0005_binary_search.py
├── 0006_intersection_of_two_arrays_ii_practice.py
├── 0007_combine_two_tables.py
├── 0008_second_highest_salary.py
├── 0009_top_k_frequent_elements.py
├── 0010_insert_delete_getrandom_o1.py
├── 0011_print_in_order.py
├── 0012_encode_decode_tinyurl.py
└── 0013_kth_largest_element_in_a_stream.py
```

## Running the Solutions
```bash
# Run a specific solution
python solutions/0001_single_number.py

# Run all solutions
for file in solutions/*.py; do
    echo "Running $file"
    python "$file"
    echo "---"
done
```

## Key Learning Points
1. **XOR Operations**: Efficient for finding unique elements in pairs
2. **Cycle Detection**: Using sets to detect cycles in sequences
3. **Frequency Counting**: Hashmaps for character/number frequency analysis
4. **Binary Search**: Logarithmic time search in sorted arrays
5. **SQL Joins**: LEFT JOIN for preserving all records from primary table
6. **Heap Data Structure**: Maintaining top-k elements efficiently
7. **O(1) Operations**: Combining arrays and hashmaps for constant time operations
8. **Thread Synchronization**: Locks and semaphores for controlled execution order
9. **Hashmap Storage**: Efficient key-value lookups for caching and mapping
10. **Stream Processing**: Real-time algorithms for handling data streams

## Next Steps for Interview Preparation
1. Review system design concepts (URL shortener, rate limiter, caching)
2. Practice API design with FastAPI or Flask
3. Study database indexing and query optimization
4. Review Python-specific features (generators, decorators, context managers)
5. Practice mock interviews focusing on communication and problem-solving approach