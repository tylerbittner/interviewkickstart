
def compute_intersection(a, b):
    '''Assumes input lists a and b are SORTED'''

    if len(a) == 0 or len(b) == 0:
        return []

    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        print('DEBUG: i, j =', i, j)
        # case 1
        if a[i] < b[j]:
            i += 1
        # case 2
        elif a[i] > b[j]:
            j += 1
        # case 3: a[i] == b[j]
        else:
            if i == 0 or a[i] != a[i-1]:
                result.append(a[i])
            i += 1
            j += 1
    return result


a = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
b = [5, 5, 6, 8, 8, 9, 10, 10]
print('Calling compute_intersection()...')
output = compute_intersection(a, b)
print('Expected output: [5, 6, 8]')
print('Intersection of a and b:', output)