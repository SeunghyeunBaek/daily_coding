--����17��)	film ���̺��� Ȱ���Ͽ�,  rental_duration ��  7�� �̻� �뿩�� ������  film �� ���ؼ�  film_id,   title,  description �÷��� Ȯ���غ�����.	
select 
	film_id
	, title
	, description
	, rental_duration 
from film f 
where
	rental_duration >= 7
order by 
	rental_duration
	, film_id;