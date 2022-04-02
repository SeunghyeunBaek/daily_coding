--문제1번) dvd 렌탈 업체의  dvd 대여가 있었던 날짜를 확인해주세요.
----2005-05-24~2006-02-14
select 
	distinct cast(rental_date as date) as rental_date_ymd
from rental r
order by rental_date_ymd;