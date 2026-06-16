select today.id id
from Weather today 
inner join Weather yesterday
on datediff(today.recordDate, yesterday.recordDate) = 1 and 
today.temperature > yesterday.temperature;