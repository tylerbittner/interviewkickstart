def selection_sort(a):

    for i in range(len(a)):
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
result = selection_sort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

# EDGE CASES
a = [14, 2]
result = selection_sort(a)
assert result == [2, 14]

a = [2]
result = selection_sort(a)
assert result == [2]

a = []
result = selection_sort(a)
assert result == []