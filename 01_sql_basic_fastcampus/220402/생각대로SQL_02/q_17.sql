--문제17번) 고객의 성에 John 이라는 단어가 들어가는, 고객의 이름과 성을 모두 찾아주세요.	
select 
	first_name
	, last_name
from customer c 
where
	first_name like '%John%';