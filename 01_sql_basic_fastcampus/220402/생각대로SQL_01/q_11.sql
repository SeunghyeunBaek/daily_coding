--문제11번)	영화배우의 이름 (이름+' '+성) 에 대해서,  대문자로 이름을 보여주세요.  단 고객의 이름이 동일한 사람이 있다면,  중복 제거하고, 알려주세요.	
select
	distinct on (upper(first_name||' '||last_name))
	actor_id
	, upper(first_name||' '||last_name) as full_name
	, first_name 
	, last_name 
from actor