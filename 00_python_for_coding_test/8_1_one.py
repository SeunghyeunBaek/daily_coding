
def main(input_):
    x = int(input_)

    """
    ai = min(ai, ai/2, ai/3, ai/5) + 1
    """
    mem = [0] * (x+1)

    for i in range(2, x+1):

        mem[i] = mem[i-1] +  1

        if i % 2==0:
            mem[i] = min(mem[i], mem[i//2] + 1)

        if i % 3==0:
            mem[i] = min(mem[i], mem[i//3] + 1)

        if i % 5==0:
            mem[i] = min(mem[i], mem[i//5] + 1)

    return mem[x]

if __name__ == '__main__':
    
    input_ = """26"""
    output = main(input_)
    print(output)