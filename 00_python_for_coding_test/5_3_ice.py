"""얼음 얼리기
* DFS
"""

from itertools import product

def main(input_):
	global hole, block, visited, map_	

	hole, block, visited = '0', '1', 'x'
	n_rows, n_cols, map_ = parse_input(input_)
	cnt = 0
	for row_id, col_id in product(range(n_rows), range(n_cols)):
		
		visited_pos = []
		is_blocked = fill_hole(row_id, col_id, visited_pos)

		if not is_blocked:
			cnt = cnt+1
			print(f"----Count +1: {cnt}")
			print(f"----Visited: {visited_pos}")

	return cnt 

def fill_hole(row_id, col_id, visited_pos):
	global hole, block, visited, map_

	# Exit condition
	if is_outside([row_id, col_id], len(map_), len(map_[0])):
		return True

	if map_[row_id][col_id] == hole:
		map_[row_id][col_id] = visited
		visited_pos.append([row_id, col_id])

		print(f"Visited: {row_id} {col_id}")
		print_map(map_)

		fill_hole(row_id+1, col_id, visited_pos)
		fill_hole(row_id-1, col_id, visited_pos)
		fill_hole(row_id, col_id+1, visited_pos)
		fill_hole(row_id, col_id-1, visited_pos)
		
		return False

	else:
		return True

def parse_input(input_:str)->list:
	"""Parse input data
	"""
	lines = input_.split('\n')
	n_rows, n_cols = map(int, lines[0].split(' '))
	map_ = []

	for row_id in range(n_rows):
		row = [char_ for char_ in lines[1+row_id]]
		map_.append(row)

	return n_rows, n_cols, map_

def is_outside(pos, n_rows, n_cols):

	if all([0<=pos[0]<n_rows, 0<=pos[1]<n_cols]):
		return False

	else:
		return True

def print_map(map_):

	print()
	for row in map_:
		print(row)
	print()

if __name__ == '__main__':

	inputs = [
		"""4 5
00110
00011
11111
00000""",

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
11100011111111"""]

	for i, input_ in enumerate(inputs):
		print("="*30)
		print(f"input: {i}, ans: {main(input_)}")
		print("="*30)