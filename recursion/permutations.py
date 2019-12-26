
def perms_main(array):
    global counter
    counter = 1
    perms_rec(array, 0)


def perms_rec(array, i):
        '''Print all permutations of items from a[i]..a[len(array)], prefixed with items before array[i].'''

        # Base case: array fully transformed into one possible permutation
        if i == len(array):
            # print permuted array
            global counter
            print(f'{counter}: {array}')
            counter += 1
            return

        # Permute! Swap item in first position (after prefix) with each other item
        for j in range(i, len(array)):
            array[i], array[j] = array[j], array[i]
            perms_rec(array, i+1)
            # undo swap to restore array
            array[i], array[j] = array[j], array[i]


#################
# Test cases
#################
test_input = ['b', 'c', 'e', 'f']
perms_main(test_input)


test_input = ['b', 'c', 'e', 'f', 'g', 'h']
perms_main(test_input)