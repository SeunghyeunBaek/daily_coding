from time import time

def get_fibo_num(n):

    if n in [1, 2]:
        return 1

    return get_fibo_num(n-1) + get_fibo_num(n-2)

# Top down
def get_fibo_num_td(n):
    global mem

    if n in [1, 2]:
        return 1

    if mem[n] != 0:
        return mem[n]

    else:
        mem[n] = get_fibo_num_td(n-1) + get_fibo_num_td(n-2)
        return mem[n]

# Bottom up
def get_fibo_num_bt(n):
    global mem
    mem[1], mem[2] = 1, 2

    for i in range(3, n+1):
        mem[i] = mem[i-1] + mem[i-2]

    return mem[n-1]

if __name__ == '__main__':

    # Recursive fibonacci number
    global mem
    n = 40 # 50
    
    fibos = [
        get_fibo_num,
        get_fibo_num_td,
        get_fibo_num_bt
    ]

    for func in fibos:
        print(f"start: {func.__name__}")
        start = time()
        res = func(n)
        el_time = round(time() - start, 5)
        print(f"end: {func.__name__}, {res}, {el_time}")
        mem = [0]*(n+1)