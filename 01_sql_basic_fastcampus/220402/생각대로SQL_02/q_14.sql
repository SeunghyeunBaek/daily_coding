--����14��) staff ���̺��� �̿��Ͽ�, staff ��  picture  ������ ���� �ִ�  ������  id, �̸�,���� Ȯ�����ּ���.  �� �̸��� ����  �ϳ��� �÷����� �̸�, �������·�  ���ο� �÷� name �÷����� �������ּ���.	
select 
	staff_id 
	, first_name||' '||last_name as name
from staff s 
where picture is not null;