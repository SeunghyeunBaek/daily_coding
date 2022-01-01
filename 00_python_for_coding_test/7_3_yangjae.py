"""
https://junsik-hwang.tistory.com/76
"""
import time

def greedy_cut(cakes, req):

    max_cut_len = max(cakes)
    thr = [max_cut_len-x for x in cakes]
    
    for i in range(1, max_cut_len+1):
        
        cut_cakes = []

        for j, cake in enumerate(cakes):

            cut_cakes.append(i - thr[j] if i > thr[j] else 0)

        if sum(cut_cakes) >= req:

            return i, cut_cakes

    return None

def bi_cut(cakes, req):
    pass


def main(input_):
    lines = input_.split('\n')
    n_cakes, req = list(map(int, lines[0].split(' ')))
    cakes = sorted(list(map(int, lines[1].split(' '))), reverse=True)
    height, cut_cakes = greedy_cut(cakes, req)
    return height, cut_cakes


if __name__ == '__main__':
    input_ = '''4 6
19 15 10 17'''

    output = main(input_)
    print(output)