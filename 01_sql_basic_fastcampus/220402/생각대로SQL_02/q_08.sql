--����8��) payment ���̺��� �̿��Ͽ�,  ����ȣ�� 341�� �ش� �ϴ� ����� ������ 2007�� 2�� 15~16�� ���̿� �� ��� ���������� Ȯ�����ּ���.
select *
from payment p 
where
	customer_id = 341
	and cast(payment_date as date) between '2007-02-15' and '2007-02-16';