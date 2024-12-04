DIRECTIONS = [
    (0, 1),   # Horizontal right
    (0, -1),  # Horizontal left
    (1, 0),   # Vertical down
    (-1, 0),  # Vertical up
    (1, 1),   # Diagonal down-right
    (-1, -1), # Diagonal up-left
    (1, -1),  # Diagonal down-left
    (-1, 1)   # Diagonal up-right
]

def checkWord(word, grid, rows, cols, r, c, dr, dc):
    for i in range(len(word)):
        new_r = r + i * dr
        new_c = c + i * dc
        if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
            return False
        if grid[new_r][new_c] != word[i]:
            return False
    return True

def countXMAS(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    for r in range(rows):
        for c in range(cols):
            for dr, dc in DIRECTIONS:
                if checkWord("XMAS", grid, rows, cols, r, c, dr, dc):
                    count += 1
    return count

def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

filename = "input.txt"  
grid = read_grid_from_file(filename)
    
total_count = countXMAS(grid)
print(total_count)

# part 2
# gross
def checkCrossMAS(grid, r, c, rows, cols):
    if grid[r][c] == 'A':
        if r > 0 and c > 0 and r < rows - 1 and c < cols - 1:
            valid1 = grid[r-1][c-1] == 'M' and grid[r+1][c+1] == 'S' or grid[r-1][c-1] == 'S' and grid[r+1][c+1] == 'M'
            valid2 = grid[r-1][c+1] == 'M' and grid[r+1][c-1] == 'S' or grid[r-1][c+1] == 'S' and grid[r+1][c-1] == 'M'
            return valid1 and valid2
    return False

def countMAS(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    for r in range(rows):
        for c in range(cols):
            if checkCrossMAS(grid, r, c, rows, cols):
                count += 1
    return count
 
masCount = countMAS(grid)                   
print(masCount)