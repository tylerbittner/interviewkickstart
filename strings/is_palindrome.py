def is_palindrome(s):
    print(f'In is_palindrome. s={s}')
    n = len(s)
    if n <= 1:
        return True

    l = 0
    r = n-1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1

    return True



#---
# TESTS
#---
assert is_palindrome('tacocat') == True
assert is_palindrome('123321') == True
assert is_palindrome('asdf') == False
assert is_palindrome('') == True
assert is_palindrome('a') == True
