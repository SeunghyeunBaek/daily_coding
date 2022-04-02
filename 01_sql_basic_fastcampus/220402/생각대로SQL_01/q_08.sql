--문제8번) 고객의 id 가  50,100,150 ..등 50번의 배수에 해당하는 고객들에 대해서,
--회원 가입 감사 이벤트를 진행하려고합니다.
--고객 아이디가 50번 배수인 아이디와, 고객의 이름 (성, 이름)과 이메일에 대해서
--확인해주세요.	
select
	customer_id
	, first_name
	, last_name
	, email 
from
	customer
where customer_id % 50 = 0;
