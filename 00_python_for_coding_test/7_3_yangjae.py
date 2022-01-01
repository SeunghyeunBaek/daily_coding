"""
https://junsik-hwang.tistory.com/76
"""
from time import time
import random

def timer(func):
    def warpper(*args, **kwargs):
        start_ts = time()
        res = func(*args, **kwargs)
        end_ts = time()
        print(f"{func.__name__}: {round(end_ts-start_ts, 5)}s")
        return res
    return warpper

@timer
def greedy_cut(cake_heights, req_len):

    max_cutter_height = max(cake_heights)

    for cutter_height in range(0, max_cutter_height+1):

        total_cut_cake_height = 0

        for cake_height in cake_heights:

            cut_cake_height = cake_height - cutter_height if cutter_height <= cake_height else 0
            total_cut_cake_height += cut_cake_height

        # print(total_cut_cake_height)
        if total_cut_cake_height < req_len:

            return cutter_height - 1

    return cutter_height

@timer
def bi_cut(cake_heights, req_len):

    low = 0
    high = max(cake_heights)

    while low <= high:

        mid = (low + high) // 2
        
        total_cut_cake_height = 0

        for cake_height in cake_heights:

            cut_cake_height = cake_height - mid if mid <= cake_height else 0
            total_cut_cake_height += cut_cake_height

        if total_cut_cake_height > req_len:
            res = mid
            low = mid + 1

        elif total_cut_cake_height < req_len:

            high = mid - 1

    return res

def main(input_):
    # Parse input
    lines = input_.split('\n')
    n_cakes, req_len = list(map(int, lines[0].split(' ')))
    # cake_heights = sorted(list(map(int, lines[1].split(' '))), reverse=True)
    cake_heights = list(map(int, lines[1].split(' ')))
    max_cutter_height = 0

    greedy_max_cutter_height = greedy_cut(cake_heights, req_len)
    bi_max_cutter_height = bi_cut(cake_heights, req_len)

    return greedy_max_cutter_height, bi_max_cutter_height


if __name__ == '__main__':


#     input_ = '''4 6
# 19 15 10 17'''
    
    # Gernerate test case
    n_cakes = 100000
    req_len = 1
    cake_heights = [str(random.randint(1, 100)) for i in range(n_cakes)]
    cake_heights = ' '.join(cake_heights)

    # Run
    input_ = f"{n_cakes} {req_len}\n{cake_heights}"
    output = main(input_)
    print(output)