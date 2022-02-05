def main(input_):

    inputs: list = sorted(input_)
    sum_ = 0

    for i, e in enumerate(inputs):
        
        if e.isdigit():
            sum_ += eval(e)

        else:
            break
    
    res = ''.join(inputs[i:])       
    res = res + str(sum_) if sum_ != 0 else res

    return res


if __name__ == '__main__':

    input_ = 'K1KA5CB7'
    output = main(input_)