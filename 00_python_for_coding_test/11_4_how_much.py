
def get_min_invalid_amt(input_):
    lines = input_.split("\n")
    n_conins = eval(lines[0])
    coins = list(map(lambda x: eval(x.strip()), lines[1].split(" ")))
    coins.sort()

    amt = 1
    
    for coin in coins:
        if amt < coin:
            break
        amt += coin
        
    return amt


if __name__ == "__main__":
    
    input_ = """5
3 2 1 1 9"""
    output = get_min_invalid_amt(input_)
    print(output)