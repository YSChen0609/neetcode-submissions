-- This is an interesting one, playing with ORDER bY
-- can get the first ones and highest one, note only Postgres has DISTINCT ON, thus use
-- row_number() for other databases

---------------
-- ORDER BY
-- DISTINCT ON
---------------

select 
    distinct on (student_id)
    student_id,
    exam_id,
    score

from exam_results
order by student_id, score desc, exam_id asc
