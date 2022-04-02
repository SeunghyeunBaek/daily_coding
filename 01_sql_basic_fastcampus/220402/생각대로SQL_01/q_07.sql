--문제7번) 대여 기간이 (회수 - 대여일) 10일 이상이였던 rental 테이블에 대한 모든 정보를 알려주세요.
select 
	rental_id
	, rental_date
	, return_date
	, inventory_id 
	, customer_id 
	, staff_id 
	, last_update 
from rental r3
where
	cast(return_date as date) - cast(rental_date as date) + 1>= 10
order by rental_id;