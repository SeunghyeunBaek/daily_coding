
def main(input_):
    res = 0

    for num in input_:
        num = eval(num)
        res = res + num if res <= 1 or num <= 1 else res * num
    return res

if __name__ == '__main__':
    
    for input_ in ['02984', '567']:
        print(main(input_))