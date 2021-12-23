"""Sort alogorithms
1. Selection sort
2. Insertion sort
3. Quick sort
4. Counting sort
"""
from time import perf_counter
from contextlib import contextmanager
import random

import sys
sys.setrecursionlimit(10**5)

@contextmanager
def timer(name):
    """
    with timer('func'):
        func()
    """
    start = perf_counter()
    yield
    end = perf_counter()
    print(f'[{name}] done in {end-start:.5f}s')

def selection_sort(arr):

    for i in range(len(arr)):
        min_value_index = i

        for j in range(i+1, len(arr)):

            if arr[min_value_index] > arr[j]:
                min_value_index = j
        arr[i], arr[min_value_index] = arr[min_value_index], arr[i]
    return arr

def quick_sort(array):

    """
    RecursionError: maximum recursion depth exceeded in comparison
    import sys
    sys.setrecursionlimit(10**7)
    """
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

def insertion_sort(arr):

    for i in range(1, len(arr)):

        for j in range(i, 0, -1):

            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

            else:
                break
    return arr

def counting_sort(arr):
    count = [0] * (max(arr)+1)
    res = []
    for i in range(len(arr)):
        count[arr[i]] += 1

    for i in range(len(arr)):

        for j in range(count[i]):
            res.append(i)
    return res

if __name__ == '__main__':

    # arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    n_elements = 20
    arr = [random.randint(0, n_elements) for i in range(n_elements)]

    funcs = [
        'selection_sort',
        'insertion_sort',
        'quick_sort',
        'counting_sort'
    ]

    results = list()

    for func in funcs:
        with timer(func):
            res = eval(func)(arr)
            results.append(res)
            # print(f"res: {res}")