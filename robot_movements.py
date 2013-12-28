# Created by JiaYi Lim on 24/12/2013

import copy

def initialize(rows, cols):
    '''Set up the grid and the starting position of the robot'''
    grid = [ [ 0 for c in range(cols) ] for r in range(rows) ] # cells are all 0 to start off with, i.e. unvisited
    pos_r = 0
    pos_c = 0
    print move_robot(grid, pos_r, pos_c)

def move_robot(grid, r, c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]):
        return 0 # outside of the grid
    elif grid[r][c] == 1:
        return 0 # cell has already been visited
    elif r == len(grid)-1 and c == len(grid[0])-1:
        return 1 # reached the destination cell
    else:
        grid[r][c] = 1 # set the cell to visited
        # need to create deep copies for each recursive call so that the original matrix is not affected
        grid_up = copy.deepcopy(grid)
        grid_down = copy.deepcopy(grid)
        grid_left = copy.deepcopy(grid)
        grid_right = copy.deepcopy(grid)
        return move_robot(grid_down, r+1, c) + move_robot(grid_up, r-1, c) + move_robot(grid_left, r, c-1) + move_robot(grid_right, r, c+1)


if __name__ == '__main__':
    initialize(4, 4)