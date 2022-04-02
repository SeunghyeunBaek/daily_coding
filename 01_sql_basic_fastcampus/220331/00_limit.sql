--00 Limit: 출력하는 행 수 제한
--limtit n offset m: m+1 row 부터 n개 출력
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
	
--내림차순
select
	film_id
	, title
	, rental_rate 
from
	film f2 
order by rental_rate desc
	limit 100
;