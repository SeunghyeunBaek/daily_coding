--����14��)	rental ���̺��� Ȱ���Ͽ�,  ���� return �ߴ� ��¥�� 2005��6��20�Ͽ� �ش��ߴ� rental �� ������ ������� Ȯ���غ�����.	
select
	count(rental_id)
from
	rental r 
where
	cast(return_date as date) = '2005-06-20'
;