# Write your MySQL query statement below
SELECT Employee.name AS Employee 
FROM Employee 
WHERE Employee.Salary > (
  SELECT mgr.Salary FROM Employee AS mgr
  WHERE mgr.id = Employee.managerId
)