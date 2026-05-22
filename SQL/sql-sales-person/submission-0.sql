-- Write your query below
with
made_order_sales as
(
    select sales_id
    from orders o join company c on o.com_id=c.com_id
    where c.name='CRIMSON'
)

select name
from sales_person
where sales_id not in (select * from made_order_sales)
