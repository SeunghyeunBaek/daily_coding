
def main(inputs_):
    lines = inputs_.split('\n')
    n, k = list(map(int, lines[0].split(' ')))
    a = sorted(list(map(int, lines[1].split(' '))))
    b = sorted(list(map(int, lines[2].split(' '))), reverse=True)

    for i in range(k):

        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break
            
    return sum(a)



if __name__ == '__main__': 
    inputs_ = """5 3
1 2 5 4 3
5 5 6 6 5
"""
    output = main(inputs_)
    print(output)