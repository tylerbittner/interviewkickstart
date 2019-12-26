from random import randrange

def quicksort(a):

    if len(a) <= 1:
        return a

    quicksort_rec(a, 0, len(a)-1)
    print(f'Returning: {a}')
    return a


def quicksort_rec(a, start, end):

    print(f'DEBUG: a={a}')
    # base case
    if start >= end:
        return

    # Lomuto's partitioning
    rando = randrange(start, end+1)
    pivot_val = a[rando]
    a[start], a[rando] = a[rando], a[start]
    lo = start
    for hi in range(start+1, end+1):
        print(f'DEBUG in for loop: a={a}')
        print(f'DEBUG: len(a)={len(a)}, lo={lo}, hi={hi}.  pivot_val={pivot_val}, a[hi]={a[hi]}')
        if a[hi] < pivot_val:
            lo += 1
            a[lo], a[hi] = a[hi], a[lo]
            
    # Put pivot into found proper location
    a[start], a[lo] = a[lo], a[start]
    print(f'Result after sorting around {pivot_val}: {a[start:end+1]}')

    # Run again on lo & hi sides, excluding pivot
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