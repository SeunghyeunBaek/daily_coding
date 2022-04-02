--문제18번)	film 테이블을 활용하여,  rental_duration   대여가 가능한 일자가 3일 또는 5일에 해당하는  film_id,  title, desciption 을 확인해주세요.	
select 
	film_id
	, title
	, description
	, rental_duration 
from film f 
where
	rental_duration in (3, 5)
order by 
	rental_duration
	, film_id;