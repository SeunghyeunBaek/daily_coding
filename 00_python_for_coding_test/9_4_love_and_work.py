"""
dep: departure
dst: destination
"""

from itertools import product

INF = float('inf')
DEBUG = False

def main(input_):

    dep_company = 1
    n_companies, n_roads, dst_company, layover_company, times = parse_input(input_)

    log(f"Init time table")
    log(f"departure: {dep_company}, layover: {layover_company}, destiantion: {dst_company}")
    log_graph(times)
    
    company_combs = product(range(1, n_companies+1), range(1, n_companies+1), range(1, n_companies+1))

    for dep_company_, layover_company_, dst_company_ in company_combs:
        direct_time_ = times[dep_company_][dst_company_]
        layover_time_ = times[dep_company_][layover_company_] + times[layover_company_][dst_company_]
        times[dep_company_][dst_company_] = min(direct_time_, layover_time_)

    log(f"Optimized time table")
    log_graph(times)

    total_time = times[dep_company][layover_company] + times[layover_company][dst_company]
    output = -1 if total_time == float('inf') else total_time

    return output

def parse_input(input_):
    lines = input_.split('\n')
    n_companies, n_roads = list(map(int, lines[0].split(' ')))
    layover_company, dst_company = list(map(int, lines[-1].split(' ')))

    times = [[INF]*(n_companies+1) for _ in range(n_companies+1)]

    for i, line in enumerate(lines[1:-1]):

        dep_company_, dst_company_ = list(map(int, line.split(' ')))
        times[dep_company_][dst_company_] = 1
        times[dst_company_][dep_company_] = 1  # Bidirection

    for dep_company_, dst_company_ in zip(range(n_companies+1), range(n_companies+1)):
        times[dep_company_][dst_company_] = 0

    return n_companies, n_roads, dst_company, layover_company, times


def log(msg, debug=DEBUG):
    print(msg) if debug else None

def log_graph(graph):

    for i in graph:
        log(i)

if __name__ == '__main__':

    inputs = [
"""5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5""",
"""4 2
1 3
2 4
3 4"""]

    for input_ in inputs:
        output = main(input_)
        print(output)