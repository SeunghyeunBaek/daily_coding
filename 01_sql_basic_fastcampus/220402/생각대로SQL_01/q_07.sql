--����7��) �뿩 �Ⱓ�� (ȸ�� - �뿩��) 10�� �̻��̿��� rental ���̺� ���� ��� ������ �˷��ּ���.
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