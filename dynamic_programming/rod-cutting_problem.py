# Rod-cutting problem

#cache = [None]

def max_price(rod_length, prices):

    # Base case    
    if rod_length == 0:
        return 0

    # if cache[rod_length] is not None:
    #     return cache[legth]

    result = prices[rod_length]
    for i in range(1, rod_length):
        result = max(result, prices[i] + max_price(rod_length - i, prices))
    # cache[rod_length] = result
    return result


def max_price_DPiter(rod_length, prices):

    best_prices = [-1] * rod_length
    best_prices[0] = 0
    #best_prices[1] = 2
    for curr_length in range(1, rod_length + 1):
        result = prices[curr_length]
        for i in range(1, curr_length):
            result = max(result, prices[i] + best_prices[curr_length - 1])

        best_prices[curr_length] = result

    return best_prices[rod_length]


rod_length = 6
length_prices = [0, 2, 5, 5, 11, 11, 9]

output = max_price(rod_length, length_prices)
print(f'max_price() output={output}')

output = max_price_DPiter(rod_length, length_prices)
print(f'max_price_DPiter() output={output}')
