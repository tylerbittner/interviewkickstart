def reverse_string_inplace(s):
    '''
    time: O(n)
    space: O(n) -- due to immutability of strings in python; O(1) otherwise
    '''
    n = len(s)
    if n <= 1:
        return s

    l = 0
    r = n - 1

    s_list = list(s)
    while l < r:
        s_list[l], s_list[r] = s_list[r], s_list[l]
        l += 1
        r -= 1

    # GOTCHA WATCH!!! We must return the new result since assignment inside a function makes it *local* only.
    s = ''.join(s_list)
    return s


#---
# TESTS
#---
s = ''
s = reverse_string_inplace(s)
assert s == ''

s = 'a'
s = reverse_string_inplace(s)
assert s == 'a'

# odd # of items
s = 'abc'
s = reverse_string_inplace(s)
assert s == 'cba'

# even # of items
s = 'blahhi'
s = reverse_string_inplace(s)
assert s == 'ihhalb'