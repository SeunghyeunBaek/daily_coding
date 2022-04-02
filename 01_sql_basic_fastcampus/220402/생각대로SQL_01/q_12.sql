--문제12번)	고객 중에서,  active 상태가 0 인 즉 현재 사용하지 않고 있는 고객의 수를 알려주세요.	
select
	count(customer_id)
from 
	customer c
where 
	activebool = false;
--limit 1
--;