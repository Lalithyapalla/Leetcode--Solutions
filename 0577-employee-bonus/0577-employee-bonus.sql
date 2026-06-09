SELECT 
    Employee.name, 
    (SELECT Bonus.bonus FROM Bonus WHERE Bonus.empId = Employee.empId) AS bonus
FROM Employee
WHERE 
    Employee.empId NOT IN (SELECT Bonus.empId FROM Bonus WHERE Bonus.empId IS NOT NULL)
    OR  Employee.empId IN (SELECT Bonus.empId FROM Bonus WHERE Bonus.bonus < 1000);