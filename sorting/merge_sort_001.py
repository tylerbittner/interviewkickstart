# merge_sort.py

from math import floor

def merge_sort(a):
    '''Intro into recursive function.'''

    if len(a) <= 1:
        return a

    merge_sort_rec(a, 0, len(a)-1)
    return a


def merge_sort_rec(a, start, end):
    '''Recursive method that does the work'''

    if start >= end:
        # Sublist is sorted
        return

    # Recurse
    mid = floor((start + end)/2)
    merge_sort_rec(a, start, mid)
    merge_sort_rec(a, mid + 1, end)

    # Merge
    l = start
    r = mid + 1
    aux = []

    # QUESTION: Why = here instead of just < ???

    while l <= mid and r <= end:
        if a[l] <= a[r]:
            aux.append(a[l])
            l += 1
        else:
            aux.append(a[r])
            r += 1
    # Add remaining from either side
    while l <= mid:
        aux.append(a[l])
        l += 1
    while r <= end:
        aux.append(a[r])
        r += 1

    # Update sublist w/ merged list
    a[start:end+1] = aux



a = [14, 2, 8, 3, 5, 45, 6, 12]
result = merge_sort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

# EDGE CASES
a = [14, 2]
result = merge_sort(a)
assert result == [2, 14]

a = [2]
result = merge_sort(a)
assert result == [2]

a = []
result = merge_sort(a)
assert result == []