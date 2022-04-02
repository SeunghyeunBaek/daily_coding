--문제13번)	Customer 테이블을 활용하여,  store_id = 1 에 매핑된  고객의 수는 몇명인지 확인해보세요.	
select 
	count(customer_id)
from
	customer c 
where
	store_id = 1;