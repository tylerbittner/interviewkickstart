from random import randrange

def quicksort(a):
    if len(a) <= 1:
        print(f'Returning a: {a}')
        return a

    quicksort_rec(a, 0, len(a)-1)
    print(f'Returning a: {a}')
    return a

def quicksort_rec(a, start, end):

    # base case
    if start >= end:
        return

    # Do Lomuto's partitioning
    rand = randrange(start, end+1)
    pivot_val = a[rand]
    a[rand], a[start] = a[start], a[rand]
    low = start
    for hi in range(start+1, end+1):
        if a[hi] < pivot_val:
            low += 1
            a[low], a[hi] = a[hi], a[low] 
    a[start], a[low] = a[low], a[start]

    quicksort_rec(a, start, low-1)
    quicksort_rec(a, low+1, end)




#------------------------------------------------------------------------------
# TESTS
#------------------------------------------------------------------------------

# Run these mult. times cause of the random pivot 
a = [14, 2, 8, 3, 5, 45, 6, 12]
result = quicksort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 2, 8, 3, 5, 45, 6, 12]
result = quicksort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 2, 8, 3, 5, 45, 6, 12]
result = quicksort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

# EDGE CASES
a = [14, 2]
result = quicksort(a)
assert result == [2, 14]

a = [2]
result = quicksort(a)
assert result == [2]

a = []
result = quicksort(a)
assert result == []