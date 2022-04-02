-- 00 전체 조회
select *
	from customer c 

;
-- ctr + shift + e: 실행계획

-- 01 컬럼 조회, alias
-- alias 쓰면 성능이 좋음
select -- 실행순서 3
	first_name -- 실행순서 4
	, last_name
	, c.email
	from   -- 실행순서 1
		customer c --실행순서 2
;



	