--00 Limit: ����ϴ� �� �� ����
--limtit n offset m: m+1 row ���� n�� ���
select
	film_id
	, title
	, release_year 
from
	film f2 
order by film_id 
	limit 5
	offset 10
;
	
--��������
select
	film_id
	, title
	, rental_rate 
from
	film f2 
order by rental_rate desc
	limit 100
;