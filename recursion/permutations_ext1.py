import sys

globalcounter = 1


def perms_ext1_main(a):
    '''Main function calling recursive function'''
    print(f'Printing permutations of "{a}"')
    perms_ext1_recursive(a, 0)


def perms_ext1_recursive(a, i):
    '''Print alternating odd/even permutations of given array'''
    # print(f'DEBUG perms_ext1_recursive(): a={a}, i={i}')

    # Base case
    if i == len(a) - 1:
        global globalcounter
        print(f'\t\tbase case {globalcounter}: a = {a}')
        globalcounter += 1
        return

    # Iterate and recurse
    for j in range(i, len(a)):
        # print(f'\tDEBUG: j={j}')
        a = swap_items(a, i, j)
        # Recurse
        perms_ext1_recursive(a, i + 1)
        # Undo swap
        a = swap_items(a, i, j)


def swap_items(a, i, j):
    '''Helper to swap to items in array'''

    # print(f'\tDEBUG: swapping... original a = {a}, i={i}, j={j}')
    a[i], a[j] = a[j], a[i]
    # print(f'\tDEBUG: swapped a = {a}')
    return a


# Hardcoded test cases
# inputs = [12, 34, 1234, 5678]
# for test_a in inputs:
#    perms_ext1_main(test_a)


# Or read test cases from stdin
with sys.stdin as f:
    for line in f.readlines():
        line = line.rstrip()
        perms_ext1_main(list(line))