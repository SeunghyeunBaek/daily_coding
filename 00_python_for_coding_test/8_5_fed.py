
def main(input_):
    # parse input
    lines = input_.split('\n')
    n_coins, amt = list(map(int, lines[0].split(' ')))
    coins = [int(coin) for coin in lines[1:]]

    # 모르겠음 ㅜㅜ

if __name__ == '__main__':
    input_ = """2 15
2
3"""
    output = main(input_)