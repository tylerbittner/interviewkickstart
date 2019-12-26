def bubble_sort(a):
    n = len(a)
    if n <= 1:
        return

    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break




#------------------------------------------------------------------------------
# TESTS
#------------------------------------------------------------------------------

a = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(a)
assert a == [11, 12, 22, 25, 34, 64, 90]

a = [14, 2, 8, 3, 5, 45, 6, 12]
bubble_sort(a)
assert a == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 2, 8, 3, 5, 6, 45, 12]
bubble_sort(a)
assert a == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 45, 6, 2, 8, 3, 5, 12]
bubble_sort(a)
assert a == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 2]
bubble_sort(a)
assert a == [2, 14]

a = [2]
bubble_sort(a)
assert a == [2]

a = []
bubble_sort(a)
assert a == []