from collections import deque
grid = [
        ['W','L','L','L','L','W'],
        ['W','L','M','M','T','W'],
        ['W','L','W','W','T','W'],
        ['W','L','W','T','T','W'],
        ['W','L','L','L','L','W'],
        ['W','W','W','W','W','W']
]
def simulate(grid,disaster_type,startX,startY):
    lookup = set()
    c = 0
    q = deque()
    q.append((startX,startY))
    disaster_affect_dict = {'C':{'W','M'},'D':{'L','M'},'F':{'W','L'}}
    if grid[startX][startY] not in disaster_affect_dict[disaster_type]:
        return 0
    moves = [(-1,0),(0,-1),(1,0),(0,1)]
    while q:
        pathX,pathY = q.popleft()
        for xi,yi in moves:
            x,y = pathX+xi,pathY+yi
            while True:
                if 0 <= x < len(grid) and 0 <= y < len(grid):
                    if (x,y) in lookup:
                        break
                    if grid[x][y] in disaster_affect_dict[disaster_type]:
                        c += 1
                        lookup.add((x,y))
                        q.append((x,y))
                    else:
                        break
                else:
                    break
    return c

print(simulate(grid,'C',0,0))
