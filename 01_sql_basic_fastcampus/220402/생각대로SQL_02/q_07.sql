--문제7번) address 테이블을 이용하여, 우편번호(postal_code) 값이  두번째글자가 1인 우편번호의  address_id, address, district ,postal_code  컬럼을 확인해주세요.	
select address_id
	   , address
	   , district
	   , postal_code
from
	address a 
where postal_code like '_1%'