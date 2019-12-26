def merge_sort(a):

    if len(a) <= 1:
        print(f'Returing a: {a}')
        return a
    merge_sort_rec(a, 0, len(a)-1)

    print(f'Returing a: {a}')
    return a

def merge_sort_rec(a, start, end):

    # Base case
    if start >= end:
        return

    mid = (start + end) // 2
    merge_sort_rec(a, start, mid)
    merge_sort_rec(a, mid+1, end)

    # merge
    aux = []
    i = start
    j = mid+1
    while i <= mid and j <= end:
        if a[i] <= a[j]:
            aux.append(a[i])
            i += 1
        else:
            aux.append(a[j])
            j += 1
    # append remaining items in either subarray
    while i <= mid:
        aux.append(a[i])
        i += 1
    while j <= end:
        aux.append(a[j])
        j += 1
    a[start:end+1] = aux


#------------------------------------------------------------------------------
# TESTS
#------------------------------------------------------------------------------

a = [14, 2, 8, 3, 5, 45, 6, 12]
result = merge_sort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 2, 8, 3, 5, 6, 45, 12]
result = merge_sort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 45, 6, 2, 8, 3, 5, 12]
result = merge_sort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 2]
result = merge_sort(a)
assert result == [2, 14]

a = [2]
result = merge_sort(a)
assert result == [2]

a = []
result = merge_sort(a)
assert result == []