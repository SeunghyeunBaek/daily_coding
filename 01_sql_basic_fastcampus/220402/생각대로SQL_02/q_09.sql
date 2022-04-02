--문제9번) payment 테이블을 이용하여, 고객번호가 355에 해당 하는 사람의 결제 금액이 1~3원 사이에 해당하는 모든 결제 내역을 확인해주세요.	
select *
from payment p 
where
	customer_id = 355
	and amount between 1 and 3;