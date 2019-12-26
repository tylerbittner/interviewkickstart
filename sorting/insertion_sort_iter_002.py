def insertion_sort_iter(a):
    if len(a) <= 1:
        return a

    for i in range(1, len(a)):
        ins_val = a[i]
        j = i-1
        while j >= 0 and a[j] > ins_val:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = ins_val

    return a



#------------------------------------------------------------------------------
# TESTS
#------------------------------------------------------------------------------

a = [14, 2, 8, 3, 5, 45, 6, 12]
result = insertion_sort_iter(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 2, 8, 3, 8, 5, 45, 8, 6, 12]
result = insertion_sort_iter(a)
assert result == [2, 3, 5, 6, 8, 8, 8, 12, 14, 45]

# EDGE CASES
a = [14, 2]
result = insertion_sort_iter(a)
assert result == [2, 14]

a = [2]
result = insertion_sort_iter(a)
assert result == [2]

a = []
result = insertion_sort_iter(a)
assert result == []