--문제9번) 영화 제목의 길이가 8글자인, 영화 제목 리스트를 나열해주세요.	
select title
from film f 
--where title like '________';
where char_length(title) = 8
order by title