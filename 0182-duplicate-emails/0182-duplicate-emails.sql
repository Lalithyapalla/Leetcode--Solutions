select distinct p.email AS Email
from Person p
where (select count(*) from Person duplicate
where duplicate.email = p.email) > 1;