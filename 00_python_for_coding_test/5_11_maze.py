from collections import deque

def main(input_, debug=False):
    n_rows, n_cols, map_ = parse_input(input_)
    road, wall = 1, 0
    pos = [0, 0]
    # NESW
    drow = [-1, 0, 1, 0]
    dcol = [0, 1, 0, -1]

    q = deque()
    q.append(pos)

    while q:

        pos = q.popleft()

        print(f"[info] current pos: {pos}") if debug else None
        print_map(map_) if debug else None

        for d in range(4):
            dst_row = pos[0] + drow[d]
            dst_col = pos[1] + dcol[d]

            if not all([0<=dst_row<n_rows, 0<=dst_col<n_cols]):
                print(f"[continue] outside map d:{d} {dst_row},{dst_col} > {n_rows}x{n_cols}") if debug else None
                continue
            
            node_state = map_[dst_row][dst_col]

            if node_state == wall:
                print(f"[continue] wall d:{d} {dst_row},{dst_col}") if debug else None
                continue
            
            if node_state == road:
                map_[dst_row][dst_col] = map_[pos[0]][pos[1]] + 1
                q.append([dst_row, dst_col])
                print(f"[go] d:{d} {dst_row}, {dst_col}") if debug else None
                print(f"[go] update distance: {map_[dst_row][dst_col]}") if debug else None
                print_map(map_) if debug else None

    return map_[n_rows-1][n_cols-1]


def parse_input(input_):
    lines = input_.split('\n')
    n_rows, n_cols = list(map(int, lines[0].split(' ')))
    map_ = [list(map(int, lines[x])) for x in range(1, 1+n_rows)]
    return n_rows, n_cols, map_

def print_map(map_):

    for row in map_:
        print(row)

if __name__ == '__main__':

    inputs = [
        """4 6
101111
101010
101011
111011""",
        """4 6
110110
110110
111111
111101"""]
    
    for input_ in inputs:
        ans = main(input_, debug=True)
        print("-"*10)
        print(f"Ans: {ans}")