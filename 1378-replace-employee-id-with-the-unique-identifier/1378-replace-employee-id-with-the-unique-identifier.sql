select uni.unique_id , e.name from Employees as e
left join EmployeeUNI as uni
on uni.id = e.id;