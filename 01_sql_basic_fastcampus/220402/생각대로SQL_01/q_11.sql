--����11��)	��ȭ����� �̸� (�̸�+' '+��) �� ���ؼ�,  �빮�ڷ� �̸��� �����ּ���.  �� ���� �̸��� ������ ����� �ִٸ�,  �ߺ� �����ϰ�, �˷��ּ���.	
select
	distinct on (upper(first_name||' '||last_name))
	actor_id
	, upper(first_name||' '||last_name) as full_name
	, first_name 
	, last_name 
from actor