--문제11번) film 테이블을 이용하여,  film의 길이가  100~120 에 해당하거나 또는 rental 대여기간이 3~5일에 해당하는 film 의 모든 정보를 확인해주세요.	
select *
from film f 
where
	length between 100 and 120
	and rental_duration between 3 and 5;