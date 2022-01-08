"""
    * 왼쪽부터 창고를 조진다고 가정
    * i 번 창고를 조지기 전, 아래 두가지 경우 중 식량을 더 많이 얻을 수 있는 경우를 선택해야함
        - i번창고 + i-2번창고 조지기
        - i-1번창고 조지기
    * ai = max(ai-1, ai-2+ki)
        - ai: i번째 창고까지 조진결과 쌓인 식량합의 최댓값
        - ki: k번째 창고에 들어있는 식량수
"""

def main(input_):
    # Parse input
    lines = input_.split('\n')
    n_storages = int(lines[0])
    foods = list(map(int, lines[1].split(' '))) 

    # Set dp table
    d = [0] * n_storages
    d[0] = foods[0]
    d[1] = max(d[0], foods[1])

    # Attack
    for i in range(2, n_storages):

        d[i] = max(d[i-2]+foods[i], d[i-1])
    
    # print(d)
    
    return d[n_storages-1]

if __name__ == '__main__':
    
    input_ = """4
1 3 1 5"""

    output = main(input_)

    print(output)
    