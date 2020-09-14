# Imagine a robot sitting on the upper left corner of grid with r rows and c columns. The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.
# 1's in the grid are "navigateable" and 0's are not.
# Recursive Solution
    # I first started off on this problem by separating the fact that I need to return the path and finding whether or not there exists a path
    # First solve the problem of just telling if there is a path to the end. Base Condition: Out of grid, return false and if current position is the end return True.
    # Then, Recurse right and down (or condition in the return statement takes care of that)
    # For getting the actual path traversed, I used the stack, putting the current position (row, col) onto the stack when I am in it and popping it if that function returns
# Recursive Solution with Memoization
    # For memoization, I introduced the seen set, if the position I am in has already been passed through previously, then, obviously, it cannot lead to the end goal. 
    # No, the end goal isn't moksha (https://en.wikipedia.org/wiki/Moksha). It is the bottom left element of the grid.
    # This change will take runtime from O(2^(m*n)) in recursive to O(m*n) because we hit each element just once.

# Neat!, No? 
    
def robot_in_a_grid_recursive(grid):
    seen = set()
    stack = []
    def robot_in_a_grid_helper(grid, pos):
        if pos in seen:
            stack.pop()
            return False
        seen.add(pos)
        row, col = pos
        nrow = len(grid)
        ncol = len(grid[0])
        if row >= nrow or col >= ncol or grid[row][col] == 0:
            return False
        if row == nrow - 1 and col == ncol - 1:
            stack.append(pos)
            print(stack)
            return True
        if grid[row][col] == 1:
            stack.append(pos)
            return robot_in_a_grid_helper(grid, (row + 1, col)) or robot_in_a_grid_helper(grid, (row, col + 1))
        stack.pop()
        return False

    return robot_in_a_grid_helper(grid, (0,0))

# Wrote this to randomly create grids
# import random
# grid = []
# for i in range(10):
#     row = []
#     for j in range(10):
#         row.append(random.randrange(0,2,1))
#     grid.append(row)

grid = [[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,0,0,0,0,0],[1,1,1,1,1,1]]
print(robot_in_a_grid_recursive(grid))