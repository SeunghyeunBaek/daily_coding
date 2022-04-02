
--00 where
--ctr + shift + f: ÀÚµ¿ indent
select
	first_name ,
	last_name
from
	customer c
where
	first_name = 'Jamie'
	and last_name = 'Rice';
	
select 
	customer_id
	, amount
	, payment_date
from payment p2 
where
	amount <= 1 or amount >= 8;