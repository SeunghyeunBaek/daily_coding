--문제5번) 영화 카테고리 중에서 ,Sci-Fi  카테고리의  카테고리 번호는 몇번인가요?	
select 
	category_id
	, name
from category c 
where 
	name = 'Sci-Fi';