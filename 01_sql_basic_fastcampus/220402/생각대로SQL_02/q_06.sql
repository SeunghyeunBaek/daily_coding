--����6��) address ���̺��� �̿��Ͽ�, �����ȣ(postal_code) ���� 77�� �����ϴ�  �ּҿ� ���Ͽ�, address_id, address, district ,postal_code  �÷��� Ȯ�����ּ���.	
select
	address_id
	, address
	, district 
	, postal_code
from address a 
where
	postal_code like '77%';