def bubble_sort(a):

    for end in range(len(a)-1, 0, -1):
        swapped = False
        for j in range(0, end):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            print(f'Breaking early. end={end}')
            break

    print(f'Returning a: {a}')
    return a


#------------------------------------------------------------------------------
# TESTS
#------------------------------------------------------------------------------

a = [14, 2, 8, 3, 5, 45, 6, 12]
result = bubble_sort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

# EDGE CASES
a = [14, 2]
result = bubble_sort(a)
assert result == [2, 14]

a = [2]
result = bubble_sort(a)
assert result == [2]

a = []
result = bubble_sort(a)
assert result == []