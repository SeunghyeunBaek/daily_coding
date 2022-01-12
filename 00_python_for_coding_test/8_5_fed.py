
def main(input_):
    # parse input
    lines = input_.split('\n')
    n_coins, amt = list(map(int, lines[0].split(' ')))
    coins = [int(coin) for coin in lines[1:]]

    # 모르겠음 ㅜㅜ
"""
n, m = map(int, input().split())
val = [int(input()) for _ in range(n)]
print(val)
d = [10001]*10001
d[0] = 0
for v in val:
    for j in range(v, m+1):
        d[j] = min(d[j], d[j-v]+1)
print(d[m])
"""

"""
https://techblog-history-younghunjo1.tistory.com/234
import sys

N, M = map(int, input().split())
currency = [int(input()) for _ in range(N)]
# DP 테이블
d = [10001] * (M+1)
d[0] = 0  # 0원일 경우

for c in range(len(currency)):
    for j in range(currency[c], M+1):
        if d[j - currency[c]] != 10001:
            # 화폐 단위마다 갱신
            d[j] = min(d[j], d[j - currency[c]] + 1)
 
if d[M] == 10001:
    print(-1)
else:
    print(d[M])
"""
if __name__ == '__main__':
    input_ = """2 15
2
3"""
    output = main(input_)