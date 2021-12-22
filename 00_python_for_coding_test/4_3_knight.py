import string
from itertools import product

def main(pos):
    # Parse input
    col_id, row_id = string.ascii_lowercase.index(pos[0]), int(pos[1]) - 1
    
    print(f"Input: {pos} -> {col_id},{row_id}")
    
    # Set constants
    cnt = 0
    n_rows, n_cols = 8, 8
    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    for drow, dcol in steps:

        cnt_condition = all([0<col_id + dcol<n_cols, 0<row_id + drow<n_rows])

        if cnt_condition:
            cnt += 1

    return cnt

if __name__ == '__main__':

    inputs = ['a1']

    for input_ in inputs:
        ans = main(input_)
        print(f'input: {input_} | ans: {ans}')