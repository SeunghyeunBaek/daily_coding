
def main(inputs_):
    lines = inputs_.split('\n')
    n, k = list(map(int, lines[0].split(' ')))
    a = sorted(list(map(int, lines[1].split(' '))), reverse=True)
    b = sorted(list(map(int, lines[2].split(' '))), reverse=True)
    """TODO
    """

if __name__ == '__main__': 
    inputs_ = """5 3
1 2 5 4 3
5 5 6 6 5
"""
    output = main(inputs_)
    print(output)