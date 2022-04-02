--문제15번)	film 테이블을 활용하여, 2006년에 출시가 되고 rating 이 'G' 등급에 해당하며, 대여기간이 3일에 해당하는  것에 대한 film 테이블의 모든 컬럼을 알려주세요.	
select *
from
	film f 
where
	release_year = '2006'
	and rating = 'G'
	and rental_duration = 3
order by film_id;
