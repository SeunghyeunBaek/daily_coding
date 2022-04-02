--00 in
select 
	customer_id 
	, rental_id
	, return_date 
from rental r 
where
	customer_id in (1, 2)
order by return_date, customer_id desc;

--01 or
select
	customer_id ,
	rental_id
from
	rental r2
where
	customer_id = 1
	or customer_id = 2
order by
	rental_date ,
	customer_id desc;
	
--02 not in
select
	customer_id
	, rental_id
	, return_date
from
	rental r 
where
	customer_id not in (1, 2)
order by return_date desc;

--03 and 
select
	customer_id
	, rental_id
	, return_date
from
	rental r 
where
	customer_id <> 1
	and customer_id <>2
order by return_date desc;

--04 sub query
select 
	first_name
	, last_name
from 
	customer c2
where 
	customer_id in (
						select
							customer_id
						from
							rental r 
						where
							cast(return_date as date) = '2005-5-27'
					);


