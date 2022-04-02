-- 00 order by: 정렬
-- asc: 오름차순 desc: 내림차순
select 
	first_name 
	, last_name 
	from 
		customer c 
	order by first_name asc
			, last_name desc
	;
	
-- 01 컬럼순서로 order by 지정할 수 있음
select 
	first_name 
	, last_name 
	from 
		customer c 
	order by 1 asc
			, 2 desc
	;