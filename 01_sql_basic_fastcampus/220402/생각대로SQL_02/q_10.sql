--문제10번) customer 테이블을 이용하여, 고객의 이름이 Maria, Lisa, Mike 에 해당하는 사람의 id, 이름, 성을 확인해주세요.	
select 
	customer_id
	, first_name
	, last_name
from customer c 
where first_name in ('Maria', 'Lisa', 'Mike');