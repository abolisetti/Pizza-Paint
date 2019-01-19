#Flood Fill.py

def fill(grid,x,y,oldv,newv):
    if grid[x][y] == oldv:
        grid[x][y] == newv
        fill(grid, x + 1, oldv, newv)
        fill(grid, x - 1, oldv, newv)
        fill(grid, x, oldv + 1, newv)
        fill(grid, x, oldv - 1, newv)
fill(grid,1,1,0,2)
pprint(grid)
