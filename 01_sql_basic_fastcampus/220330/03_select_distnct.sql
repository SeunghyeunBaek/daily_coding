--00 select distinct: 중복 제거
-- distinct a, b: a,b 동시 중복 제거
	
--01 테이블 생성
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

-- 조회
select *
from t2;

-- 테이블 삭제
--drop table t2;

--02 중복제거
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
