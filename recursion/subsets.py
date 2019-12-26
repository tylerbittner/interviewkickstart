
def print_subsets_main(a):
    '''Entry point into function'''
    global counter
    counter = 1
    s = [None] * len(a)
    subsets_rec(a, 0, s, 0)


def subsets_rec(a, i, s, j):
    ''' Get all subsets of array a.  Params:
    a: original char array
    i: index to start at getting subsets of
    s: "prefix" or "subset so far"
    j: index to end prefix at in s
    '''
    #print(f'DEBUG: a={a}, i={i}, s={s}, j={j}')

    # base case
    if i == len(a):
        global counter
        print(f'subset {counter}: {s[:j]}')
        counter += 1 
        # print(f'\tDEBUG - full subset s={s}')
        return

    # Decision point 1: get subsets w/out a[i]
    subsets_rec(a, i+1, s, j)

    # Decision point 2: get subsets WITH a[i] as a prefix
    s[j] = a[i]
    subsets_rec(a, i+1, s, j+1)


def print_subsets_main_practice(a):

    subset_so_far = [None] * len(a)
    subsets_rec_practice(a, 0, subset_so_far, 0)


def subsets_rec_practice(a, i, s, j):

    # base case:
    if i == len(a):
        print('subset:', s[:j])
        return
    # get subsets WITHOUT a[i]
    subsets_rec_practice(a, i+1, s, j)
    # get subsets WITH a[i]
    s[j] = a[i]
    subsets_rec_practice(a, i+1, s, j+1)



# Number of subsets will be 2^n
input = ['t', 'c', 'd', 'o']
print('Calling print_subsets_main()...')
print_subsets_main(input)

print('Calling print_subsets_main_practice()...')
print_subsets_main_practice(input)
