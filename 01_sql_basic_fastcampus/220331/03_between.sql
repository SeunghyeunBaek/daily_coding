--00 between a and b  a<=x<=b
--not between a and b x<a or x>b
select
	customer_id 
	, payment_id 
	, amount 
from
	payment p 
where
	amount between 8 and 9
--	amount not between 8 and 9
order by
	amount 
--offset 10 limit 100
	
	
--01 날짜 비교
select
	customer_id
	, payment_id
	, amount
	, payment_date
	, cast(payment_date as date) as cast_
	, to_char(payment_date, 'yyyy-mm-dd') as to_char_
from
	payment p 
where
	cast(payment_date as date) between '2007-02-07' and '2007-02-15'
--	to_char(payment_date, 'yyyy-mm-dd') between '2007-02-07' and '2007-02-15'
order by payment_date;