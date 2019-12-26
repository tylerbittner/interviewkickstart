import sys
import os

########## I/O CODE END


def check_if_sum_possible(arr, k):
    subset = []
    res = check_if_sum_possible_rec(arr, 0, subset, k)
    return res


def check_if_sum_possible_rec(arr, i, subset, k):
    print(f'DEBUG: Inputs to _rec(arr, i, subset, k) are ({arr}, {i}, {subset}, {k})')

    # base case: exhausted possible subsets
    # if i == len(arr):
    #     print(f'Sum of subsets == k NOT POSSIBLE')
    #     return 0

    # base case:
    if len(subset) > 0 and sum(subset) == k:
        print(f'Sum of subset ({subset}) == k')
        return 1

    # Try subset withOUT next item in arr
    check_if_sum_possible_rec(arr, i + 1, subset, k)

    # Try subset WITH next item in arr
    subset.append(arr[i])
    check_if_sum_possible_rec(arr, i + 1, subset, k)

    return 0


########## I/O CODE START
if __name__ == "__main__":
    f = sys.stdout

    arr_cnt = 0
    arr_cnt = int(input())
    arr_i = 0
    arr = []
    while arr_i < arr_cnt:
        arr_item = int(input());
        arr.append(arr_item)
        arr_i += 1


    k = int(input());

    res = check_if_sum_possible(arr, k);
    f.write(str(int(res)) + "\n")


    f.close()

########## I/O CODE END

# Test inputs:
'''
YES
3
2
4
8
6

YES
3
8
4
2
6

NO
3
2
4
8
5

YES
1
0
0

NO
1
1
0
'''


