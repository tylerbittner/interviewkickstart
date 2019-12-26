# selection_sort.py

def selection_sort_rec(a, i):

    # base case
    if i < 0:
        return a

    selection_sort_rec(a, i-1)
    
    min = i
    for j in range(i+1, len(a)):
        if a[j] < a[min]:
            min = j
    a[i], a[min] = a[min], a[i]

    return a


#------------------------------------------------------------------------------
# TESTS
#------------------------------------------------------------------------------

a = [14, 2, 8, 3, 5, 45, 6, 12]
result = selection_sort_rec(a, len(a)-1)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

# EDGE CASES
a = [14, 2]
result = selection_sort_rec(a, len(a)-1)
assert result == [2, 14]

a = [2]
result = selection_sort_rec(a, len(a)-1)
assert result == [2]

a = []
result = selection_sort_rec(a, len(a)-1)
assert result == []