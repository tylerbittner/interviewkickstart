def selection_sort(a):

    print(f'len(a)={len(a)}')

    for i in range(len(a)):
        print(f'i={i}')
        smallest = i
        for j in range(i+1, len(a)):
            print(f'\tj={j}')
            if a[j] < a[smallest]:
                smallest = j
        a[smallest], a[i] = a[i], a[smallest]
        print(f'\t\ta={a}')

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