--����9��) ��ȭ ������ ���̰� 8������, ��ȭ ���� ����Ʈ�� �������ּ���.	
select title
from film f 
--where title like '________';
where char_length(title) = 8
order by title