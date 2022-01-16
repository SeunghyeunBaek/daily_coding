# Gridy dijkstra
DEBUG = True

def main(input_):
    start_node, n_nodes, n_edges, graph, visited, min_distances = parse_input(input_)

    # Initiate distances for the start node
    min_distances[start_node] = 0
    visited[start_node] = True

    msg = f"""[Parsed input]
- start node: {start_node}
- n_nodes, n_edges: {n_nodes}, {n_edges}
- visited: {visited}
- min_distances: {min_distances}"""
    log(msg)
    log_current_status(graph, visited, min_distances)

    for [dst_node, distance_] in graph[start_node]:
        min_distances[dst_node] = distance_
     
    # Iteration for all nodes except start node
    for i in range(n_nodes-1):

        # Get nearest node and check visited flag
        current_node = get_nearest_node(start_node, n_nodes, min_distances, visited)
        visited[current_node] = True

        # Check layovers and update min distance
        for dst_node, distance_ in graph[current_node]:

            layover_distance = min_distances[current_node] + distance_

            if layover_distance < min_distances[dst_node]:
                min_distances[dst_node] = layover_distance

        log(f"[iter {i}]")
        log_current_status(graph, visited, min_distances)

    return min_distances

def get_nearest_node(start_node, n_nodes, min_distances, visited):
    min_distance_ = float('inf')
    nearest_node = 0

    for node in range(start_node, n_nodes+1):

        if not visited[node] and min_distances[node] < min_distance_:

            min_distance_ = min_distances[node]
            nearest_node = node

    return nearest_node

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
    min_distances = [float('inf')] * (n_nodes+1)

    return start_node, n_nodes, n_edges, graph, visited, min_distances

def log(msg ,debug=DEBUG):
    print(msg) if debug else None

def log_current_status(graph, visited, min_distances):
    log("[Current status]")
    log(f"- min distances: {min_distances}")
    log(f"- visited: {visited}")
    # log(f"- graph")

    # for node, distances_to_node in enumerate(graph):
    #     log(f"-- {node}")

    #     for dst_node, distance_ in distances_to_node:
    #         log(f"--- {dst_node}: {distance_}")

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