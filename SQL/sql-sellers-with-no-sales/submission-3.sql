-- Write your query below
with 
sold_in_2020 as
(
select seller_id
from seller join orders using(seller_id)
where EXTRACT (YEAR from sale_date) = '2020'
        and
      order_id is not NULL
)

select seller_name
from seller
where seller_id not in (select * from sold_in_2020)
order by seller_name