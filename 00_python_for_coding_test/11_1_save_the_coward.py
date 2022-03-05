
def main(input_:str):
    _, fears = parse_input(input_)
    fears.sort()

    n_cowards_in_a_group = 0
    n_groups = 0

    for fear in fears:
        n_cowards_in_a_group += 1
        
        if n_cowards_in_a_group >= fear:
            n_groups += 1
            n_cowards_in_a_group = 0
    
    return n_groups
    
def parse_input(input_:str):
    lines:list = input_.split('\n')
    n_cowards:int = eval(lines[0].strip())
    fears:list = [eval(_fear.strip()) for _fear in lines[1].split(' ')]
    return n_cowards, fears

if __name__ == '__main__':
    input_ = """5
2 3 1 2 2"""
    max_n_groups = main(input_)
    print(max_n_groups)