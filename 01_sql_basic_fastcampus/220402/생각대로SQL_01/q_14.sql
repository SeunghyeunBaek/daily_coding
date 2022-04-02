--문제14번)	rental 테이블을 활용하여,  고객이 return 했던 날짜가 2005년6월20일에 해당했던 rental 의 갯수가 몇개였는지 확인해보세요.	
select
	count(rental_id)
from
	rental r 
where
	cast(return_date as date) = '2005-06-20'
;