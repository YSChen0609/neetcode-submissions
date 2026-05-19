with 
a as 
(
    select customer_id
    from orders
    where product_name = 'A'
),
b as 
(
    select customer_id
    from orders
    where product_name = 'B'
),
c as 
(
    select customer_id
    from orders
    where product_name = 'C'
)

select distinct customer_id, customer_name
from customers join orders using (customer_id)
where customer_id in (select customer_id from a) 
        and
      customer_id in (select customer_id from b)
        and
      customer_id not in (select customer_id from c)
order by customer_name