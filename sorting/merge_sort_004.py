

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