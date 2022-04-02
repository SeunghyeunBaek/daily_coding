--문제18번) 주소 테이블에서, address2 값이 null 값인 row 전체를 확인해볼까요?
select *
from address a 
where
	address2 is null;