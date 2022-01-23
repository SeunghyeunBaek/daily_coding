# dijkstra heap
import heapq
import sys

DEBUG = True
INF = float('inf')

def main(input_):
    start_node, n_nodes, n_edges, graph, visited, min_distances = parse_input(input_)

    # Initiate distances for the start node
    min_distances[start_node] = 0
    # visited[start_node] = True

    msg = f"""[Parsed input]
- start node: {start_node}
- n_nodes, n_edges: {n_nodes}, {n_edges}
- visited: {visited}  -- deprecated
- min_distances: {min_distances}"""
    log(msg)
    log_current_status(graph, visited, min_distances)   

    # Start
    q = list()
    heapq.heappush(q, (0, start_node))

    while q:
        log_current_status(graph, visited, min_distances)
        distance, current_node = heapq.heappop(q)

        if min_distances[current_node] < distance:
            continue

        for dst_node, distance_ in graph[current_node]:
            layover_distance = distance + distance_

            if layover_distance < min_distances[dst_node]:
                min_distances[dst_node] = layover_distance
                heapq.heappush(q, (layover_distance, dst_node))

def parse_input(input_):
    lines = list(map(lambda x: x.split(' '), input_.split('\n')))
    n_nodes, n_edges = list(map(int, lines[0]))
    start_node = int(lines[1][0])
    
    # Set graph
    # graph = [[]] * (n_nodes+1)
    # https://stackoverflow.com/questions/33990673/how-to-create-a-list-of-empty-lists/33990750
    graph = [[] for i in range(n_nodes+1)]

    for line in lines[2:]:
        src_node, dst_node, distance = list(map(int, line))
        graph[src_node].append([dst_node, distance])

    visited = [False] * (n_nodes+1)
    min_distances = [INF] * (n_nodes+1)

    return start_node, n_nodes, n_edges, graph, visited, min_distances

def log(msg ,debug=DEBUG):
    print(msg) if debug else None

def log_current_status(graph, visited, min_distances):
    log("[Current status]")
    log(f"- min distances: {min_distances}")
    # log(f"- visited: {visited}")

if __name__ == '__main__':

    input_ = """6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2"""

    min_distances = main(input_)
    print(min_distances)