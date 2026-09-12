"""
LeetCode 176: Second Highest Salary
https://leetcode.com/problems/second-highest-salary/

Problem:
Table: Employee
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key column for this table.

Write a SQL query to report the second highest salary from the Employee table. 
If there is no second highest salary, return null (return None in Pandas).

Solution Approach:
Use subquery to find the maximum salary, then find the maximum salary that is less than this value.
Alternatively, use ORDER BY and LIMIT/OFFSET, or use DISTINCT with LIMIT.

Time Complexity: Depends on database implementation, typically O(n log n for sorting)
Space Complexity: O(1) for the result
"""

# Solution 1: Using subquery (most common approach)
SECOND_HIGHEST_SALARY_SQL_1 = """
SELECT 
    MAX(salary) AS SecondHighestSalary
FROM 
    Employee
WHERE 
    salary < (SELECT MAX(salary) FROM Employee);
"""

# Solution 2: Using ORDER BY and LIMIT/OFFSET
SECOND_HIGHEST_SALARY_SQL_2 = """
SELECT 
    (SELECT DISTINCT salary
     FROM Employee
     ORDER BY salary DESC
     LIMIT 1 OFFSET 1) AS SecondHighestSalary;
"""

# Solution 3: Using LIMIT with OFFSET and handling NULL case
SECOND_HIGHEST_SALARY_SQL_3 = """
SELECT 
    CASE 
        WHEN (SELECT COUNT(DISTINCT salary) FROM Employee) >= 2
        THEN (SELECT DISTINCT salary 
              FROM Employee 
              ORDER BY salary DESC 
              LIMIT 1 OFFSET 1)
        ELSE NULL
    END AS SecondHighestSalary;
"""

# Solution 4: Using subquery with NOT IN (less efficient but illustrative)
SECOND_HIGHEST_SALARY_SQL_4 = """
SELECT 
    MAX(salary) AS SecondHighestSalary
FROM 
    Employee
WHERE 
    salary NOT IN (SELECT MAX(salary) FROM Employee);
"""

def explain_solutions():
    """
    Explain the different approaches to find second highest salary.
    """
    explanations = {
        "Solution 1 (Subquery)": """
        - Find the maximum salary in the table
        - Then find the maximum salary that is less than this value
        - Handles NULL case naturally (returns NULL if no second highest)
        """,
        
        "Solution 2 (ORDER BY LIMIT)": """
        - Get distinct salaries ordered descending
        - Skip the first (highest) and take the second
        - Returns NULL if no second highest exists
        """,
        
        "Solution 3 (Explicit NULL handling)": """
        - Explicitly check if at least 2 distinct salaries exist
        - More verbose but very clear about intent
        """,
        
        "Solution 4 (NOT IN)": """
        - Exclude the highest salary and find max of remaining
        - Less efficient due to NOT IN subquery
        """
    }
    
    return explanations

# Test data simulation
def simulate_second_highest_salary():
    """
    Simulate the SQL query results with sample data.
    """
    # Test case 1: Normal case with multiple salaries
    employees1 = [
        {"id": 1, "salary": 100},
        {"id": 2, "salary": 200},
        {"id": 3, "salary": 300}
    ]
    
    # Test case 2: Duplicate salaries
    employees2 = [
        {"id": 1, "salary": 100},
        {"id": 2, "salary": 100},
        {"id": 3, "salary": 200}
    ]
    
    # Test case 3: Only one salary
    employees3 = [
        {"id": 1, "salary": 100}
    ]
    
    # Test case 4: Empty table
    employees4 = []
    
    def get_second_highest(employees):
        if not employees:
            return None
        
        # Get unique salaries
        unique_salaries = list(set(emp["salary"] for emp in employees))
        unique_salaries.sort(reverse=True)
        
        # Return second highest if exists, else None
        return unique_salaries[1] if len(unique_salaries) >= 2 else None
    
    test_cases = [
        ("Multiple salaries", employees1),
        ("Duplicate salaries", employees2),
        ("Single salary", employees3),
        ("Empty table", employees4)
    ]
    
    results = {}
    for name, employees in test_cases:
        results[name] = get_second_highest(employees)
    
    return results

# Test cases
if __name__ == "__main__":
    print("SQL Queries for Second Highest Salary:")
    print("=" * 50)
    print()
    
    print("Solution 1 (Subquery):")
    print(SECOND_HIGHEST_SALARY_SQL_1.strip())
    print()
    
    print("Solution 2 (ORDER BY LIMIT):")
    print(SECOND_HIGHEST_SALARY_SQL_2.strip())
    print()
    
    print("Solution 3 (Explicit NULL handling):")
    print(SECOND_HIGHEST_SALARY_SQL_3.strip())
    print()
    
    print("Solution 4 (NOT IN):")
    print(SECOND_HIGHEST_SALARY_SQL_4.strip())
    print()
    
    print("Explanations:")
    print("=" * 50)
    explanations = explain_solutions()
    for method, explanation in explanations.items():
        print(f"{method}:")
        print(explanation.strip())
        print()
    
    print("Simulation Results:")
    print("=" * 50)
    results = simulate_second_highest_salary()
    for case, result in results.items():
        print(f"{case}: {result}")