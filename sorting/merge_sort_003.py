from math import floor


def merge_sort(a):

    if len(a) <= 1:
        return a
    
    merge_sort_rec(a, 0, len(a)-1)
    print(f'Returning a: {a}')
    return a


def merge_sort_rec(a, start, end):

    # base case
    if start >= end:
        return

    mid = floor((end + start) / 2 )
    merge_sort_rec(a, start, mid)
    merge_sort_rec(a, mid+1, end)

    # merge two sides
    aux = []
    l = start
    r = mid+1
    while l <= mid and r <= end:
        if a[l] <= a[r]:
            aux.append(a[l])
            l += 1
        else:
            aux.append(a[r])
            r += 1
    while l <= mid:
        aux.append(a[l])
        l += 1
    while r <= end:
        aux.append(a[r])
        r += 1

    a[start:end+1] = aux



#------------------------------------------------------------------------------
# TESTS
#------------------------------------------------------------------------------

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