# quicksort01.py

import random

def quicksort01(a):
    quicksort_rec(a, 0, len(a)-1)
    print(f'Returning: {a}')
    return a

def quicksort_rec(a, start, end):
    if start >= end:
        return
    # Do Lomuto's partitioning
    rand_int = random.randint(start, end)
    pivot_val = a[rand_int]
    a[start], a[rand_int] = a[rand_int], a[start]
    smaller_ptr = start
    for bigger_ptr in range(start+1, end+1):
        # Case: value at bigger_ptr < than pivot value, therefore increase smaller_ptr by one and move the value there
        if a[bigger_ptr] < pivot_val:
            smaller_ptr += 1
            a[smaller_ptr], a[bigger_ptr] = a[bigger_ptr], a[smaller_ptr]
    a[smaller_ptr], a[start] = a[start], a[smaller_ptr]

    quicksort_rec(a, start, smaller_ptr)
    quicksort_rec(a, smaller_ptr+1, end)



# TESTS - Run these mult. times cause of the random pivot

a = [14, 2, 8, 3, 5, 45, 6, 12]
result = quicksort01(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 2, 8, 3, 5, 45, 6, 12]
result = quicksort01(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 2, 8, 3, 5, 45, 6, 12]
result = quicksort01(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

# EDGE CASES
a = [14, 2]
result = quicksort01(a)
assert result == [2, 14]

a = [2]
result = quicksort01(a)
assert result == [2]

a = []
result = quicksort01(a)
assert result == []