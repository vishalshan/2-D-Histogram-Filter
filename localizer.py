import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    print(height)
    width = len(grid[0])
    print(width)
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    b = []
    c = []
    Sum = 0
    
    for i in range(0,len(grid)):
        a = []
        for j in range(0,len(grid[0])):
            if grid[i][j] == color:
                a.append(p_hit*beliefs[i][j])
            else: 
                a.append(p_miss*beliefs[i][j])
        b.append(a)
        Sum = Sum + sum(a)
        
    for i in range(0,len(b)):
        for j in range(0,len(b[0])):
            b[i][j] = b[i][j]/Sum

        
    return b

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % height
            new_j = (j + dx ) % width
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)