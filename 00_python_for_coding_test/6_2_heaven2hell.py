
def main(input_):
    # parse input
    lines = list(map(int, input_.split('\n')))
    n_nums = lines[0]
    nums = map(str, sorted(lines[1:], reverse=True))
    nums = ' '.join(nums)
    return nums

if __name__ == '__main__':
    input_ = """3
15
27
12"""
    ans = main(input_)
    print(ans)