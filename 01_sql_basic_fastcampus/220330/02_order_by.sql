-- 00 order by: ����
-- asc: �������� desc: ��������
select 
	first_name 
	, last_name 
	from 
		customer c 
	order by first_name asc
			, last_name desc
	;
	
-- 01 �÷������� order by ������ �� ����
select 
	first_name 
	, last_name 
	from 
		customer c 
	order by 1 asc
			, 2 desc
	;