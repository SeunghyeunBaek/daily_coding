"""얼음 얼리기
Stack, Recursive

"""
from itertools import product

def main(input_):
	
	n_rows, n_cols, map_ = parse_input(input_)
	start_pos = [0, 0]
	cnt = 0

	for row_id, col_id in product(range(n_rows), range(n_cols)):

		visited_node = fill_hole_stack([row_id, col_id], map_) # TODO
		# visited_node = fill_hole_recursive() # TODO 

	return cnt 


def parse_input(input_:str)->list:
	"""Parse input data
	"""
	lines = input_.split('\n')
	n_rows, n_cols = map(int, lines[0].split(' '))
	map_ = []

	for row_id in range(n_rows):
		row = list(map(int, lines[1+row_id].split(' ')))
		map_.append(row)

	return n_rows, n_cols, map_

def is_outside(pos, n_cols, n_rows):

	if all([0<=pos[0]<n_rows, 0<=pos[1]<n_cols]):
		return False

	else:
		return True 

# TODO: dfs stack
def fill_hole_stack(root_node, map_):

	global hole, block, visited, moving_map

	# Initiate stack
	visited_nodes = [root_node]

	while visited_nodes:
		
		print(f"visited nodes: {visited_nodes}")
		cur_node = visited_nodes.pop()
		node_state = map_[cur_node[0]][cur_node[1]]
		print(f"current node: {cur_node}, {node_state}")
		if (node_state != visited) and (node_state == hole):

			map_[cur_node[0]][cur_node[1]] = visited

			for direction in range(4):

				dst_node = [cur_node[0] + moving_map[direction][0],
							cur_node[1] + moving_map[direction][1]]

				if (dst_node != visited) and (node_state == hole):
					visited_nodes.append(dst_node)

	return visited_nodes

#TODO: dfs recursive
def fill_hole_recursive():
	return None




if __name__ == '__main__':

	global hole, block, visited, moving_map
	hole, block, visited = '0', '1', 'x'
	moving_map = {0: [0, -1], 1: [1, 0], 2: [0, 1],3: [-1, 0]}

	inputs = [
		"""4 5
		0 0 1 1 0
		0 0 0 1 1
		1 1 1 1 1
		0 0 0 0 0""",
		"""15 14
		00000111100000
		11111101111110
		11011101101110
		11011101100000
		11011111111111
		11011111111100
		11000000011111
		01111111111111
		00000000011111
		01111111111000
		00011111111000
		00000001111000
		11111111110011
		11100011111111
		11100011111111"""
	]

	for i, input_ in enumerate(inputs):
		print(i, main(input_))
