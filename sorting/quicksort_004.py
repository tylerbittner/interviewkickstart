import random 


def quicksort(a):
    if len(a) <= 1:
        return a

    quicksort_rec(a, 0, len(a)-1)
    return 1


def quicksort_rec(a, start, end):

    if start >= end:
        return

    # Lumoto's partitioning
    rando = random.randrange(start, end+1)
    pivot_val = a[rando]
    a[start], a[rando] = a[rando], a[start]
    lo = start
    for hi in range(start+1, end+1):
        if a[hi] < pivot_val:
            lo += 1
            print(f'lo={lo}, hi={hi}')
            a[lo], a[hi] = a[hi], a[lo]
    a[start], a[lo] = a[lo], a[start]

    quicksort_rec(a, start, lo-1)
    quicksort_rec(a, lo+1, end)


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