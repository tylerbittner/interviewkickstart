# practice_problem-3sum.py
# Complete the function below.

def findZeroSum(arr):
    
    n = len(arr)
    if n < 3:
        return []
    
    result = []
    arr.sort()
    for i in range(n-2):
        # check for dups in i slot
        if i > 0 and arr[i] == arr[i-1]:
            continue
        lo = i+1
        hi = n-1
        #print(f'i,lo,hi == {i},{lo},{hi}')
        while lo < hi:
            sum = arr[i] + arr[lo] + arr[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                result.append(f'{arr[i]},{arr[lo]},{arr[hi]}')
                # move both pointers
                lo += 1
                hi -= 1
                # check for dups in lo/hi slots.  Could be multiple!!
                while arr[lo] == arr[lo-1] and lo < hi:
                    lo += 1
                while arr[hi] == arr[hi+1] and hi > lo:
                    hi -= 1
    return result
    

print(findZeroSum([0,0,0]))