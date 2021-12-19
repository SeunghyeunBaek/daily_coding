"""4-4 게임 개발
"""
def main(input_):

	# Parse input data
	n_rows, n_cols, cur_row_id, cur_col_id, cur_d, map_ = parse_input(input_)
	
	print(f"""----Set inputs
	- n_rows, n_cols: {n_rows}, {n_cols}
	- cur_pos: {cur_row_id}, {cur_col_id}
	- cur_direction: {cur_d}""")
	print_map(map_)

	# Set grid state
	land, sea, visited = '0', '1', 'x'
	
	# Start travel
	cnt = 0		 # Number of visited grids
	try_cnt = 0  # Go exit condition if try count is 4
	
	while True:

		#--- Exit condition
		if try_cnt == 4:
			print(f"---- Get exit condition")
			print(f"	- try_cnt: {try_cnt}")
			print(f"	- cur_pos: {cur_row_id}, {cur_col_id}")
			print(f"	- cur_direction: {cur_d}\n")

			back_row_id, back_col_id = move([cur_row_id, cur_col_id], cur_d, foward=False)
			exit_condition = any([is_outside(back_row_id, back_col_id, n_rows, n_cols),
								  map_[back_row_id][back_col_id]==sea])

			#--- Exit
			if exit_condition:
				print(f"----Exit {cur_row_id},{cur_col_id} -> {back_row_id},{back_col_id}\n")
				print_map(map_)
				return cnt + 1

			#--- Move backward
			else:
				cur_row_id, cur_col_id = back_row_id, back_col_id
				try_cnt = 0
				print(f"----Move backward to {back_row_id}, {back_col_id}")
				print(f"	- try_cnt: {try_cnt}\n")

		#--- Check visited grid & update direction
		map_[cur_row_id][cur_col_id] = visited  # Check visited grid
		cur_d = cur_d - 1 if cur_d != 0 else 3  # Update direction
		dst_row_id, dst_col_id = move([cur_row_id, cur_col_id], cur_d)  # Move to the direction
		
		print(f"""----Check visited grid {cur_row_id}, {cur_col_id}
	- updated direction: {cur_d}
	- destination: {dst_row_id}, {dst_col_id}""")
		print_map(map_)

		#--- check outside of the map
		if is_outside(dst_row_id, dst_col_id, n_rows, n_cols):
			try_cnt += 1
			print(f"----Checked outside map: {dst_row_id}, {dst_col_id}")
			print(f"	- try_cnt: {try_cnt}\n")
			continue

		#--- Destination is land, move forward
		if map_[dst_row_id][dst_col_id] == land:
			cur_row_id, cur_col_id= dst_row_id, dst_col_id
			cnt += 1 
			try_cnt = 0
			print(f"----Move foward land, update position")
			print(f"	- pos: {dst_row_id}, {dst_col_id}")
			print(f"	- cnt: {cnt}")
			print(f"	- try_cnt: {try_cnt}\n")

		#--- Destination is sea or visited, continue
		else:
			try_cnt += 1
			print(f"----Pass Sea or visited")
			print(f"	- pos: {dst_row_id}, {dst_col_id}")
			print(f"	- try_cnt: {try_cnt}\n")
			continue

def print_map(map_):

	n_rows = len(map_)

	for row_num in range(n_rows):
		print('\t', map_[row_num])
	print('')
	return None

def parse_input(input_):

	lines = input_.split('\n')
	n_rows, n_cols = lines[0].split(' ')
	n_rows, n_cols = int(n_rows), int(n_cols)
	cur_row_id, cur_col_id, cur_d = lines[1].split(' ')
	cur_row_id, cur_col_id, cur_d = int(cur_row_id), int(cur_col_id), int(cur_d)

	# Set map
	map_ = list()

	for row_num in range(n_rows):

		row = list()

		for col_num in range(n_cols):
			row.append(lines[2+row_num].split(' ')[col_num])	
		map_.append(row)

	return n_rows, n_cols, cur_row_id, cur_col_id, cur_d, map_

def move(pos, d, foward=True):

	if d == 0:
		pos[0] = pos[0] - 1 if foward else pos[0] + 1
	elif d == 1:
		pos[1] = pos[1] + 1 if foward else pos[1] - 1
	elif d == 2:
		pos[0] = pos[0] + 1 if foward else pos[0] -1
	elif d == 3:
		pos[1] = pos[1] - 1 if foward else pos[1] + 1

	return pos

def is_outside(row_id, col_id, n_rows, n_cols):

	if not all([0<=row_id<n_rows, 0<=col_id<n_cols]):
		return True

	else:
		return False

if __name__ == '__main__':

	input_ = """4 4
1 1 0
1 1 1 0
0 0 0 1
0 0 0 1
0 1 0 1"""
	output = main(input_)
	print(f'ans: {output}')