

def unlock(key:list, lock:list)->bool:

    unlocked = False
    n_lock_rows, n_lock_cols = len(lock), len(lock[0])
    angles = [0, 90, 180, 270]
    
    for angle in angles:

        for row_id in range(n_lock_rows):

            for col_id in range(n_lock_cols):

                rotated_key = roate_clockwise(key)
                moved_key = move(rotated_key, row_id, col_id)
                unlocked = check_unlocked(moved_key, lock)

                if unlocked:
                    break
                
    return unlocked

def roate_clockwise(key: list) -> list:
    return key

def move(key: list, row_id:int, col_id: int) -> list:
    return key

def check_unlocked(key:list, lock:list) -> bool:
    unlocked = False
    return unlocked

if __name__ == '__main__':
    
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    unlocked = unlock(key, lock)
    print(unlocked)