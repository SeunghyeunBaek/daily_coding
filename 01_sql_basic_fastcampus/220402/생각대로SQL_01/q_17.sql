--문제17번)	film 테이블을 활용하여,  rental_duration 이  7일 이상 대여가 가능한  film 에 대해서  film_id,   title,  description 컬럼을 확인해보세요.	
select 
	film_id
	, title
	, description
	, rental_duration 
from film f 
where
	rental_duration >= 7
order by 
	rental_duration
	, film_id;