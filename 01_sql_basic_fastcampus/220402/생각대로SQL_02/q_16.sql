--����16��) address ���̺��� �̿��Ͽ�, postal_code ����  �� ��(NULL) �̰ų� 35200, 17886 �� �ش��ϴ� address �� ��� ������ Ȯ�����ּ���.	
select *
from address a 
where
	postal_code is null
	or postal_code in ('35200', '17886')
order by postal_code; 