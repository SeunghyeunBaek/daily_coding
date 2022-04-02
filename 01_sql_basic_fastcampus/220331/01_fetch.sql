--00 fetch
--fetch first n row only: n건
--offset n rows fetch first m row only: n+1 행부터 m 개

select
	film_id ,
	title
from
	film f2
order by
	film_id
	offset 5 rows
	fetch first 2 row only;