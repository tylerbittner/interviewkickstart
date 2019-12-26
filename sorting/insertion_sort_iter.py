# Pnuemonic for insertion sort: 
#   Each successive item is *inserted* into it's correct spot in the sorted list to the left.


def insertion_sort_iter(a):

    if len(a) <= 1:
        return a

    for i in range(1, len(a)):
        print(f'a at i={i} is {a}')
        # save val to insert
        ins_val = a[i]
        j =  i - 1
        while j >= 0 and a[j] > ins_val:
            # shift larger val to right
            a[j+1] = a[j]
            j -= 1
        a[j+1] = ins_val

    print(f'returning {a}')
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

a = [14, 2, 8, 3, 5, 6, 45, 12]
result = insertion_sort_iter(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 45, 6, 2, 8, 3, 5, 12]
result = insertion_sort_iter(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 2]
result = insertion_sort_iter(a)
assert result == [2, 14]

a = [2]
result = insertion_sort_iter(a)
assert result == [2]

a = []
result = insertion_sort_iter(a)
assert result == []