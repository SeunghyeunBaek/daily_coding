--00 fetch
--fetch first n row only: n��
--offset n rows fetch first m row only: n+1 ����� m ��

select
	film_id ,
	title
from
	film f2
order by
	film_id
	offset 5 rows
	fetch first 2 row only;