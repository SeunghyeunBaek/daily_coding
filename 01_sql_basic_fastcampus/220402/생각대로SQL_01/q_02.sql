--����2��) ��ȭ���̰� 120�� �̻��̸鼭, �뿩�Ⱓ�� 4�� �̻��� ������, ��ȭ������ �˷��ּ���.	
select film_id
	   , title
	   , length 
	   , rental_duration 
from 
	film as f
where
	length >= 120
	and rental_duration >=4
order by film_id;