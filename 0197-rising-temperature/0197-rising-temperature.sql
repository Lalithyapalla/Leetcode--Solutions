select today.id id
from Weather today 
join Weather yesterday
where datediff(today.recordDate, yesterday.recordDate) = 1 and 
today.temperature > yesterday.temperature;