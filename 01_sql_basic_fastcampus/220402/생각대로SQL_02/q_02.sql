--����2��) actor �� ��(last_name) ��  Jo �� �����ϴ� ����� id ���� ���� ���� ��� �ѻ���� ���Ͽ�, �����  id ����  �̸�, �� �� �˷��ּ���.	
select
	actor_id
	, first_name 
	, last_name 
from actor
where
	last_name like 'Jo%'
order by actor_id
limit 1;