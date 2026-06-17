select r.contest_id ,
round(count(r.user_id)/(select count(user_id) from Users)* 100,2)
as percentage from Register r
left join Users as u
on u.user_id = r.user_id
group by r.contest_id
order by percentage desc, contest_id asc;
