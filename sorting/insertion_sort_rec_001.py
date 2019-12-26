def insertion_sort_rec(a, i):

    # base case
    if i <= 0:
        return a

    insertion_sort_rec(a, i-1)
    ins_val = a[i]
    j = i - 1
    print(f'j={j}, i={i}; ins_val={ins_val}')
    while ins_val < a[j] and j >= 0:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = ins_val

    return a



#------------------------------------------------------------------------------
# TESTS
#------------------------------------------------------------------------------

a = [14, 2, 8, 3, 5, 45, 6, 12]
result = insertion_sort_rec(a, len(a)-1)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 2, 8, 3, 8, 5, 45, 8, 6, 12]
result = insertion_sort_rec(a, len(a)-1)
assert result == [2, 3, 5, 6, 8, 8, 8, 12, 14, 45]

# EDGE CASES
a = [14, 2]
result = insertion_sort_rec(a, len(a)-1)
assert result == [2, 14]

a = [2]
result = insertion_sort_rec(a, len(a)-1)
assert result == [2]

a = []
result = insertion_sort_rec(a, len(a)-1)
assert result == []