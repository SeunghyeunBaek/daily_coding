--문제3번)film 테이블을 이용하여, film 테이블의 아이디값이 1~10 사이에 있는 모든 컬럼을 확인해주세요.	
select *
from film f 
where 
	film_id between 1 and 10;