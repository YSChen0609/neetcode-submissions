-- Write your query below

select e.*,
       case 
        when operator='>' then v1.value > v2.value
        when operator='<' then v1.value < v2.value
        when operator='=' then v1.value = v2.value
       end as value
from variables v1 join expressions e 
            on v1.name = e.left_operand
                  join variables v2
            on v2.name = e.right_operand

