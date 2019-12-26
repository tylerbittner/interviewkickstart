import random

def quickselect(a, k):
    '''Return Kth smallest element in a'''

    if len(a) == 0 or (k-1 == 0) or (k-1 >= len(a)):
        print ('Invalid input')
    else:
        return quickselect_recursive(a, k, 0, len(k) - 1)

def quickselect_recursive(a, k, start, end):

    # Base case: one-element array here
    if start == end == k - 1:
        return a[k - 1]

    # Do Lomuto's partitioning (pick a random element i & partion with elements < i on left, elements > i on the right)

    # Pick random pivot
    randindex = random.randint(start, end)

    smaller_i = index_of_pivot



    # Recursion cases
    if smaller_i == k - 1:
        return a[k-1]
    elif smaller_i < k - 1:
        # Call recursively
        return quickselect_recursive(a, k, smaller_i + 1, end)
    else:
        return quickselect_recursive(a, k, start, smaller_i - 1)