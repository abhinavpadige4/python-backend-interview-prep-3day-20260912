"""
LeetCode 175: Combine Two Tables
https://leetcode.com/problems/combine-two-tables/

Problem:
Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.

Table: Address
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.

Write a SQL query for a report that provides the following information for each person in the Person table:
FirstName, LastName, City, State

Solution Approach:
Use LEFT JOIN to combine Person table with Address table on PersonId.
This ensures all persons are included, even if they don't have an address.

Time Complexity: Depends on database implementation, typically O(n log n) for join operations
Space Complexity: O(n + m) for storing the result
"""

# SQL Solution
COMBINE_TWO_TABLES_SQL = """
SELECT 
    p.FirstName,
    p.LastName,
    a.City,
    a.State
FROM 
    Person p
LEFT JOIN 
    Address a ON p.PersonId = a.PersonId;
"""

# Alternative using LEFT JOIN explicitly
COMBINE_TWO_TABLES_ALT_SQL = """
SELECT 
    p.FirstName,
    p.LastName,
    a.City,
    a.State
FROM 
    Person p
LEFT JOIN 
    Address a 
    ON p.PersonId = a.PersonId;
"""

# Explanation of why LEFT JOIN is used:
# - We want all records from Person table (left table)
# - Matching records from Address table (right table) 
# - If no match, City and State will be NULL
# - INNER JOIN would exclude persons without addresses

# Test data simulation (for understanding)
def simulate_combine_two_tables():
    """
    Simulate the SQL query results with sample data.
    """
    # Sample Person table
    persons = [
        {"PersonId": 1, "FirstName": "Wang", "LastName": "Allen"},
        {"PersonId": 2, "FirstName": "Alice", "LastName": "Bob"}
    ]
    
    # Sample Address table
    addresses = [
        {"AddressId": 1, "PersonId": 2, "City": "New York City", "State": "New York"},
        {"AddressId": 2, "PersonId": 3, "City": "Leetcode", "State": "California"}
    ]
    
    # Simulate LEFT JOIN
    results = []
    for person in persons:
        # Find matching address
        matching_address = None
        for address in addresses:
            if address["PersonId"] == person["PersonId"]:
                matching_address = address
                break
        
        # Add to results (with NULL values if no match)
        results.append({
            "FirstName": person["FirstName"],
            "LastName": person["LastName"],
            "City": matching_address["City"] if matching_address else None,
            "State": matching_address["State"] if matching_address else None
        })
    
    return results

# Test cases
if __name__ == "__main__":
    print("SQL Query for Combine Two Tables:")
    print(COMBINE_TWO_TABLES_SQL.strip())
    print()
    
    print("Alternative SQL Query:")
    print(COMBINE_TWO_TABLES_ALT_SQL.strip())
    print()
    
    print("Simulation with sample data:")
    results = simulate_combine_two_tables()
    for i, result in enumerate(results):
        print(f"Person {i+1}: {result}")
    print()
    print("Expected Output:")
    print("- Wang Allen: City=NULL, State=NULL (no address)")
    print("- Alice Bob: City='New York City', State='New York'")