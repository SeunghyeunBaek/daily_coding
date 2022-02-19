from itertools import chain
from itertools import product
import time
def unlock(key:list, lock:list)->bool:
    
    flatten_lock = list(zip(*lock[::-1]))

    if set(flatten_lock) == {1}:
        unlocked = True
        return unlocked
    
    else:        
        unlocked = False
        n_lock_rows, n_lock_cols = len(lock), len(lock[0])
        n_key_rows, n_key_cols = len(key), len(key[0])
        degrees = [0, 90, 180, 270]
        
        try_ = product(range(-n_key_rows+1,n_lock_rows), range(-n_key_cols+1, n_lock_cols), degrees)

        for key_start_row_id, key_start_col_id, degree in try_:
            rotated_key = roate_clockwise(key, degree)
            padded_key = pad_key(rotated_key, key_start_row_id, key_start_col_id)
            unlocked = is_unlocked(padded_key, lock)
            
            if unlocked:
                break
                    
        return unlocked

def roate_clockwise(key:list, degree:int)->list:
    rotated_key = key.copy()

    for _ in range(degree//90):
        rotated_key = list(zip(*rotated_key[::-1]))

    return rotated_key

def pad_key(key:list, key_start_row_id:int, key_start_col_id:int)->list:
    padding = 0
    n_key_rows, n_key_cols = len(key), len(key[0])
    padded_key = [[padding for _ in range(n_key_cols)] for _ in range(n_key_rows)]

    for row_id, col_id in product(range(n_key_rows), range(n_key_cols)):
        refer_row_id, refer_col_id = row_id - key_start_row_id, col_id - key_start_col_id
        is_inside = all([0 <= refer_row_id < n_key_rows, 0 <= refer_col_id < n_key_cols])
        val = padding if not is_inside else key[refer_row_id][refer_col_id]
        padded_key[row_id][col_id] = val
        
    return padded_key
    
def is_unlocked(key:list, lock:list)->bool:
    unlocked = False
    flatten_key = list(chain.from_iterable(key))
    flatten_lock = list(chain.from_iterable(lock))
    unlock_checker = [_key+_lock for _key, _lock in zip(flatten_key, flatten_lock)]
    
    if set(unlock_checker) == {1}:
        unlocked = True

    return unlocked

if __name__ == '__main__':
    
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    unlocked = unlock(key, lock)
    print(unlocked)