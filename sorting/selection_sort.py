# Pnuemonic for selection sort: 
#   Iterate thru the list to *select* the next _smallest_ item to add to the end of the sorted list to the left.

def selection_sort(a):
    n = len(a)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]

    return a


#------------------------------------------------------------------------------
# TESTS
#------------------------------------------------------------------------------

a = [14, 2, 8, 3, 5, 45, 6, 12]
result = selection_sort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 2, 8, 3, 5, 6, 45, 12]
result = selection_sort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 45, 6, 2, 8, 3, 5, 12]
result = selection_sort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 2]
result = selection_sort(a)
assert result == [2, 14]

a = [2]
result = selection_sort(a)
assert result == [2]

a = []
result = selection_sort(a)
assert result == []