f = open("./day4/input.txt",'r')
grid = f.readlines()
f.close()

def solve(grid_str):
    grid = [list(line.strip()) for line in grid_str]
    rows = len(grid)
    cols = len(grid[0])

    P = [[0] * (cols + 1) for _ in range(rows + 1)]
    for r in range(rows):
        for c in range(cols):
            val = 1 if grid[r][c] == '@' else 0
            # now + up + left - up_left (double counting)
            P[r+1][c+1] = val + P[r][c+1] + P[r+1][c] - P[r][c]

    def get_area_sum(r1, c1, r2, c2):
        return P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]
    
    count_valid_elements = 0
    for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    r_min = max(0, r - 1)
                    c_min = max(0, c - 1)
                    r_max = min(rows - 1, r + 1)
                    c_max = min(cols - 1, c + 1)

                    total_in_window = get_area_sum(r_min, c_min, r_max, c_max)
                    
                    neighbors = total_in_window - 1 

                    if neighbors < 4:
                        count_valid_elements += 1

    return count_valid_elements

print(solve(grid))