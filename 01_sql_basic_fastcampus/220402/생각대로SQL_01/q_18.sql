--����18��)	film ���̺��� Ȱ���Ͽ�,  rental_duration   �뿩�� ������ ���ڰ� 3�� �Ǵ� 5�Ͽ� �ش��ϴ�  film_id,  title, desciption �� Ȯ�����ּ���.	
select 
	film_id
	, title
	, description
	, rental_duration 
from film f 
where
	rental_duration in (3, 5)
order by 
	rental_duration
	, film_id;