--����19��)	Actor ���̺��� �̿��Ͽ�,  �̸��� Nick �̰ų�  ���� Hunt ��  �����  id ��  �̸�, ���� Ȯ�����ּ���.	
select
	actor_id
	, first_name
	, last_name
from
	actor a 
where
	first_name = 'Nick'
	or last_name = 'Hunt'
order by 
	first_name 
	, last_name;
