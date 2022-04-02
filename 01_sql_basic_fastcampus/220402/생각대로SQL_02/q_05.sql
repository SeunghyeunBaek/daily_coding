--문제5번) country 테이블을 이용하여, country 이름이 s 로 끝나는 country 를 확인해주세요.	
select *
from country c 
where country like '%s';