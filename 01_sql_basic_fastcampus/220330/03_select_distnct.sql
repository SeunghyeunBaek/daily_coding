--00 select distinct: �ߺ� ����
-- distinct a, b: a,b ���� �ߺ� ����
	
--01 ���̺� ����
create table t2(id serial not null primary key, bcolor varchar, fcolor varchar);
commit;

insert
	into t2(bcolor, fcolor)
values
	('red', 'red')
	, ('red', 'red')
	, ('red', 'red')
	, ('red', null)
	, (null, 'red')
	, ('red', 'green')
	, ('red', 'blue')
	, ('green', 'red')
	, ('green', 'blue')
	, ('green', 'green')
	, ('blue', 'red')
	, ('blue', 'green')
	, ('blue', 'red');

-- ��ȸ
select *
from t2;

-- ���̺� ����
--drop table t2;

--02 �ߺ�����
select 
	distinct bcolor, fcolor
  from
  	t2
  order by
  	bcolor, fcolor;
  
--03 distinct on
select 
  distinct on (bcolor) bcolor
  					 , fcolor
  from
  	t2
  order by
  	bcolor, fcolor desc;
