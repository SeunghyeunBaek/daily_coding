--like
-- %: 모든 n 글자
-- _: 모든 1 글자
select
	first_name
	, last_name
	, first_name like 'Jen%' as jen_like
from
	customer c 
where
	first_name like '%er%';
	
--regex
select
	'FOO' like 'FOO'
	, 'BOO' like 'B__';