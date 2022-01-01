
"""
https://velog.io/@suzieep/Algorithm-%EC%9D%B4%EC%BD%94%ED%85%8C-%EB%B6%80%ED%92%88-%EC%B0%BE%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
"""

def bi_search(target, list_):

    start_id = 0
    end_id = len(list_)
    
    while True:

        # Update mid id
        mid_id = (start_id + end_id)//2

        # Exit condition
        if end_id - start_id <= 2:
            return True if list_[mid_id] == target else False

        # Update start, end id
        if list_[mid_id] == target:
            return True

        elif list_[mid_id] < target:
            start_id = mid_id + 1

        elif list_[mid_id] > target:
            end_id = mid_id - 1


def main(input_):
    lines = input_.split('\n')
    n_parts, n_reqs = int(lines[0]), int(lines[-2])
    parts = sorted(list(map(int, lines[1].split(' '))))
    reqs = list(map(int, lines[-1].split(' ')))

    res = []  # results

    for target in reqs:
        found = bi_search(target, parts)
        res.append('yes' if found else 'no')

    return ' '.join(res)

        
if __name__ == '__main__':
    
    input_ = """5
8 3 7 9 2
3
5 7 9"""
    output = main(input_)
    print(output)