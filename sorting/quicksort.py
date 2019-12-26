# quicksort.py

import random

def quicksort(a):

    if len(a) <= 1:
        print(f'Returning a: {a}')
        return a

    quicksort_rec(a, 0, len(a)-1)
    print(f'Returning a: {a}')
    return a

def quicksort_rec(a, start, end):
    
    if start >= end:
        return
    # Do Lomuto's partitioning
    rando = random.randint(start, end)
    pivot_val = a[rando]
    a[start], a[rando] = a[rando], a[start]
    low = start
    for hi in range(start+1, end+1):
        # Case: value at bigger ptr < than pivot value, therefore increase smaller ptr by one and move the value there
        if a[hi] < pivot_val:
            low += 1
             
    # Move pivot value, a[start], to it's found proper location
    a[low], a[start] = a[start], a[low]

    # Repeat process with subarrays.  Exclude the pivot cause it's in the right place now.
    quicksort_rec(a, start, low-1)
    quicksort_rec(a, low+1, end)



#------------------------------------------------------------------------------
# TESTS
#------------------------------------------------------------------------------

# Run these mult. times cause of the random pivot 
#--- Start repeat
a = [14, 2, 8, 3, 5, 45, 6, 12]
result = quicksort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 2, 8, 3, 5, 45, 6, 12]
result = quicksort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 2, 8, 3, 5, 45, 6, 12]
result = quicksort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]
#--- End repeat

a = [14, 2, 8, 3, 5, 6, 45, 12]
result = quicksort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 45, 6, 2, 8, 3, 5, 12]
result = quicksort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 2]
result = quicksort(a)
assert result == [2, 14]

a = [2]
result = quicksort(a)
assert result == [2]

a = []
result = quicksort(a)
assert result == []