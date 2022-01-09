
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
if __name__ == '__main__':
    input_ = """2 15
2
3"""
    output = main(input_)