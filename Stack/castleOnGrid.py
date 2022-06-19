from collections import deque
#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here
    lookup = set()
    c = 0
    q = deque()
    q.append((startX,startY,0))
    moves = [(-1,0),(0,-1),(1,0),(0,1)]
    while q:
        pathX,pathY,c = q.popleft()
        c += 1
        for xi,yi in moves:
            x, y = pathX,pathY
            while True:
                x,y = x+xi, y+yi
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '.':
                    if x == goalX and y == goalY:
                        return c
                    else:
                        if (x, y) not in lookup:
                            lookup.add((x,y))
                            q.append((x,y,c))
                else:
                    break
    return -1

grid = ['.X.','.X.', '...']
startX = 0
startY = 0
goalX = 0
goalY = 2
print(minimumMoves(grid, startX, startY, goalX, goalY))