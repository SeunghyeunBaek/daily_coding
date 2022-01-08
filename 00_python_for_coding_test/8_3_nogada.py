
def main(inputs):

    n_cols = int(inputs)

    d = [0] * n_cols
    d[0], d[1] = 1, 3

    for i in range(2, n_cols):

        d[i] = d[i-1] + 2*d[i-2]

    return d[n_cols-1]%796796

if __name__ == '__main__':

    inputs = """3"""
    output = main(inputs)
    print(output)