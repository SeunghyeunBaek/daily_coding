"""플로이드 워셜
Dab = min(Dab, Dak+Dkb)
"""

from itertools import product

INF = float('inf')
DEBUG = True

def main(input_):
    n_nodes, n_edges, graph = parse_input(input_)
    log(f"[input]: {n_nodes}, {n_edges}")
    log_graph(graph)
    node_combs = product(range(1, n_nodes+1), range(1, n_nodes+1), range(1, n_nodes+1))

    for layover_node_, start_node_, end_node_ in node_combs:
        layover_distance = graph[start_node_][layover_node_] + graph[layover_node_][end_node_]
        direct_distance = graph[start_node_][end_node_]
        min_distance = min(layover_distance, direct_distance)
        graph[start_node_][end_node_] = min_distance

    log(f"[output]")
    log_graph(graph)
    return graph

def parse_input(input_):
    lines = input_.split('\n')
    n_nodes, n_edges = int(lines[0]), int(lines[1])

    graph = [[INF] * (n_nodes+1) for _ in range(n_nodes+1)]

    for line in lines[2:]:
        start_node, end_node, distance = list(map(int, line.split(' ')))
        graph[start_node][end_node] = distance

    for start_node_, end_node_ in zip(range(n_nodes+1), range(n_nodes+1)):
        graph[start_node_][end_node_] = 0

    return n_nodes, n_edges, graph

def log(msg, debug=DEBUG):
    print(msg) if debug else None

def log_graph(graph):

    for row in graph: 
        log(row)

if __name__ == '__main__':

    input_ = """4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2"""
    output = main(input_)
