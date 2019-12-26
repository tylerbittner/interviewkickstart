# IK Mock challenge (was going to be presented in #3)
'''
You are given an integer array nums and you have to return a new counts array. The "counts" array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
'''

# Q: limits of len(n) and numerical size of integers?

#---
# Brute force solution
#---
def get_counts_bf(nums):

    #print(f'nums={nums}')
    n = len(nums)
    counts = [0] * n

    for i in range(n):
        for j in range(i+1, n):
            if nums[j] < nums[i]:
                counts[i] += 1

    #print(f'counts={counts}')
    return counts

'''
Time: n^2   <-- too slow
Space: n
Let's find a better solution...

*** Better approach (hopefully optimal):
- Start w/ values in counts array initialized to n-i-1, which is the number of items to the right of each
- Then sort items largest to smallest
    - Each time a nums[i] is moved to the right, subtract 1 from counts[i] since that means a larger num was to its right
    - Mergesort can be used because it's faster and stable

Time: O(nlogn) 
Space: O(n) for aux space in merge sort

'''

def get_counts(nums):

    print(f'--------------------\nOriginal nums={nums}')
    
    n = len(nums)
    counts = [i for i in range(n-1, -1, -1)]
    print(f'Original counts={counts}')

    mergesort(nums, 0, n-1, counts)

    print(f'Final nums={nums}')
    print(f'Final counts={counts}')
    return counts


def mergesort(nums, start, end, counts):

    if start >= end:
        return

    mid = (end + start) // 2
    mergesort(nums, start, mid, counts)
    mergesort(nums, mid+1, end, counts)

    # merge
    aux = []
    i = start
    j = j_orig = mid+1
    shift = 0     # Track how many positions to shift the smaller nums
    while i <= mid and j <= end:
        # Sort largest-->smallest
        if nums[i] < nums[j]:
            print(f'appending {nums[i]} at nums[{i}] to aux={aux}')
            aux.append(nums[j])
            #print(f'DEBUG: {nums[i]} is less than {nums[j]}; added 1 to shift={shift}')
            #shift += 1
            j += 1
        else:
            print(f'appending {nums[i]} at nums[{i}] to aux={aux}')
            aux.append(nums[i])
            counts[i] -= j - j_orig
            print(f'DEBUG: subtracted {j - j_orig} from counts[{i}]. New counts={counts}')
            i += 1
    while i <= mid:
        print(f'appending {nums[i]} at nums[{i}] to aux={aux}')
        aux.append(nums[i])
        counts[i] -= j - j_orig
        print(f'DEBUG: subtracted {j - j_orig} from counts[{i}]. New counts={counts}')
        i += 1
    while j <= end:
        print(f'appending {nums[i]} at nums[{i}] to aux={aux}')
        aux.append(nums[j])
        j += 1
    print(f'aux={aux}')
    nums[start:end+1] = aux



assert get_counts_bf([5,2,6,1]) == [2,1,1,0] 
assert get_counts_bf([1,2,3,4]) == [0,0,0,0]
assert get_counts_bf([4,3,2,1]) == [3,2,1,0]
assert get_counts_bf([5,6,6,1]) == [1,1,1,0] 
assert get_counts_bf([10]) == [0]
assert get_counts_bf([]) == []



assert get_counts([5,2,6,1]) == [2,1,1,0] 
assert get_counts([1,2,3,4]) == [0,0,0,0]
assert get_counts([4,3,2,1]) == [3,2,1,0]
assert get_counts([5,6,6,1]) == [1,1,1,0] 
assert get_counts([10]) == [0]
assert get_counts([]) == []