-- Write your query below
with
total_dis as
(
    select user_id, sum(distance) as travelled_distance
    from rides
    group by user_id
)

select name, coalesce(travelled_distance, 0) as travelled_distance
from users left join total_dis on users.id=total_dis.user_id
order by travelled_distance desc, name