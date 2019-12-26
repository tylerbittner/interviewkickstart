# IK mock interview #1 - "alternating chars"
# Topic: sorting
# Interviewer: Amrit Dharwadkar
# https://codebunk.com/b/1771100011120/

# Libraries Included:
# Numpy, Scipy, Scikit, Pandas
# S = "aab"
# output: "aba"
# S = "aaab"
# output: ""
#Input: "aabccccxxxxxx"
#Output: "xcxcxacxbcax"
#Output: "xcxcxcxaxacb"
# 0) ["x":6, "c":4, "a":2, "b":1]
# 1) ["x":5, "c":3, "a":2, "b":1]
# 2) ["x":4, "c":2, "a":2, "b":1]
# 3) ["x":3, "c":1, "a":2, "b":1]
# 4) ["x":2, "c":1, "a":1, "b":1]

# xcxcxcxax
# [x, c, x, a, x, b], x, c, x, a, x, c, c
# lowercase letters, max len 500

from collections import Counter

def alternate(input):
    
    counts = Counter(input)
    print(f'counts = {counts}')
    
    (char, cnt) = counts.most_common(1)[0]
    if cnt > len(input) / 2:
        return '<not possible>'
    
    result = ''
    while len(counts) >= 2:
        (char1, cnt1), (char2, cnt2) = counts.most_common(2)
        result = f'{result}{char1}{char2}'
        if cnt1 - 1 == 0:
            del counts[char1]
        else:
            counts[char1] -= 1
        if cnt2 - 1 == 0:
            del counts[char2]
        else:
            counts[char2] -= 1
    
    # Add lone remaining item
    (char1, cnt1) = counts.most_common()[0]
    result = f'{result}{char1}'
    
    return result
        

input = "aabccccxxxxxx"
print(alternate(input))
print()


input = "aabccccxxxxxxxxxxx"
print(alternate(input))
print()