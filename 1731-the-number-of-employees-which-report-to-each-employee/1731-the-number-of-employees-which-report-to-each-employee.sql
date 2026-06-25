select mgr.employee_id,mgr.name, count(emp_c.employee_id) as reports_count , 
round(avg(emp_c.age )) as average_age from Employees as mgr
join Employees as emp_c
on emp_c.reports_to = mgr.employee_id
group by mgr.employee_id, mgr.name
order by mgr.employee_id
