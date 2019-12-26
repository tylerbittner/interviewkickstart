# test1-merger_first_into_second.py

#
# Complete the merger_first_into_second function below.
#

from memory_profiler import profile

@profile(precision=9)
def merger_first_into_second(arr1, arr2):

    n1 = len(arr1)
    n2 = len(arr2)

    # Method 1 - Brute using python's built-ins. 
    # VIOLATES CONSTRAINTS because sort() does a mergesort (in most cases) which uses aux memory.
    # *This is faster than method 3 per IK's tests!!
    
    # arr2[n1:] = arr1
    # arr2.sort()

    # Method 2 - Manual pointers w/ lots of shifting slots (PARTIALLY WORKS)
    # p1 = 0
    # for p2 in range(n2):
    #     print(f'p1, p2 = {p1}, {p2} | arr1[{p1}], arr2[{p2}] = {arr1[p1]}, {arr2[p2]}')
    #     if p1 > n1-1:
    #         break
    #     elif arr2[p2] <= arr1[p1]:
    #         continue
    #     else:
    #         # Push back all greater values in n2 by one and insert the lesser value
    #         for x in range(n1+p1, p2, -1):
    #             arr2[x] = arr2[x-1]
    #         arr2[p2] = arr1[p1]
    #         p1 += 1

    # Method 3 - Optimal based on instructor's solution
    p1 = p2 = n1-1
    # p3 is where to write the val, right to left
    p3 = n2-1

    # Compare & write greater of two items in arr2 until one array is done at left
    while p1 >= 0 and p2 >= 0:
        if arr1[p1] > arr2[p2]:
            arr2[p3] = arr1[p1]
            p1 -= 1
        else:
            arr2[p3] = arr2[p2]
            p2 -= 1
        p3 -= 1

    # Write remaining of arr1 if any
    if p1 >= 0:
        arr2[:p1+1] = arr1[:p1+1]

    return arr2

# TESTS

arr1 = [1, 3, 5]
arr2 = [2, 4, 6, 0, 0, 0]
print(merger_first_into_second(arr1, arr2))
print('''Expected:
[1, 2, 3, 4, 5, 6]
''')
 

# arr1 = [1, 2, 3]
# arr2 = [4, 9, 10, 0, 0, 0]
# print(merger_first_into_second(arr1, arr2))
# print('''Expected:
# [1, 2, 3, 4, 9, 10]
# ''')

# arr1 = [4, 9, 10]
# arr2 = [1, 2, 3, 0, 0, 0]
# print(merger_first_into_second(arr1, arr2))
# print('''Expected:
# [1, 2, 3, 4, 9, 10]
# ''')

# arr1 = [11,11]
# arr2 = [3, 11, 0, 0]
# print(merger_first_into_second(arr1, arr2))
# print('''Expected:
# [3, 11, 11, 11]
# ''')

