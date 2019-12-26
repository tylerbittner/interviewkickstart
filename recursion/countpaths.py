def countpaths(grid):

    return countpaths_rec(grid, (0, 0))


def countpaths_rec(grid, curr_cell):

    paths = 0
    row, col = curr_cell

    # guard case: out of grid range
    if (row > len(grid)-1) or (col > len(grid[0])-1):
        return 0
    # base case: at destination, so found a path
    if curr_cell == (len(grid)-1, len(grid[0])-1):
        return 1
    # branch 1: move right
    paths += countpaths_rec(grid, (row, col+1))

    # branch 2: move down
    paths += countpaths_rec(grid, (row+1, col))

    return paths



input = [[None] * 3 for rows in range(3)]
print(input)
print(f'Num paths is:', countpaths(input))
