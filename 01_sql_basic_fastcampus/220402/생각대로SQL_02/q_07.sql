--����7��) address ���̺��� �̿��Ͽ�, �����ȣ(postal_code) ����  �ι�°���ڰ� 1�� �����ȣ��  address_id, address, district ,postal_code  �÷��� Ȯ�����ּ���.	
select address_id
	   , address
	   , district
	   , postal_code
from
	address a 
where postal_code like '_1%'