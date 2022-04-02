--문제19번)	Actor 테이블을 이용하여,  이름이 Nick 이거나  성이 Hunt 인  배우의  id 와  이름, 성을 확인해주세요.	
select
	actor_id
	, first_name
	, last_name
from
	actor a 
where
	first_name = 'Nick'
	or last_name = 'Hunt'
order by 
	first_name 
	, last_name;
