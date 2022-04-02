--문제4번) country 테이블을 이용하여, country 이름이 A 로 시작하는 country 를 확인해주세요.	
select *
from country 
where country like 'A%';