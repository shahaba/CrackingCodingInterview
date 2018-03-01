# Robot in a grid: find a path from top left to bottom right of the grid

def rec_paths(size, i, j, paths):
    if i >= size or j >= size:
        return

    paths[i][j] += 1
    rec_paths(size, i+1, j, paths)
    rec_paths(size, i, j+1, paths)


def find_num_paths(rows, cols):
    if rows <= 0 or cols <= 0:
        return

    paths = [[0 for i in range(cols)] for i in range(rows)]

    rec_paths(rows, 0, 0, paths)

    return paths[rows-1][cols-1]


def rec_find_path(grid, row, col, paths, invalid):

    if row < 0 or col < 0 or grid[row][col] is None:
        return False

    if (row, col) in invalid:
        return False

    if (row == 0 and col == 0) or rec_find_path(grid, row - 1, col, paths, invalid) or rec_find_path(grid, row , col - 1, paths, invalid):
        paths.append((row, col))
        return True

    invalid.append((row, col))
    return False


# Return a valid path from top left to bot right
def find_valid_path(rows, cols, invalid_grids):

    if rows <= 0 or cols <= 0:
        return

    # setup grid
    grid = [[0 for i in range(cols)] for i in range(rows)]

    # check for any invalid grids
    for invalid_grid in invalid_grids:
        i, j = invalid_grid
        grid[i][j] = None


    paths = []
    invalid = []

    rec_find_path(grid, rows-1, cols-1, paths, invalid)

    return paths


if __name__ == '__main__':
    num_paths = find_num_paths(3, 3)
    print(num_paths)

    print(find_valid_path(3, 3, [(1, 2), (1, 1)]))