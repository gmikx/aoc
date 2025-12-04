def solve_iterative(grid_input):
    grid = [row[:] for row in grid_input]
    rows = len(grid)
    cols = len(grid[0])
    
    total_removed_count = 0

    while True:
        P = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                val = 1 if grid[r][c] == '@' else 0
                P[r+1][c+1] = val + P[r][c+1] + P[r+1][c] - P[r][c]

        def get_area_sum(r1, c1, r2, c2):
            return P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]

        to_remove = []
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    r_min = max(0, r - 1)
                    c_min = max(0, c - 1)
                    r_max = min(rows - 1, r + 1)
                    c_max = min(cols - 1, c + 1)

                    # how many rolls in neighborhoor
                    total_in_window = get_area_sum(r_min, c_min, r_max, c_max)
                    
                    neighbors = total_in_window - 1 

                    if neighbors < 4:
                        to_remove.append((r, c))

        # nothing to do
        if not to_remove:
            break

        # delete @
        for r, c in to_remove:
            grid[r][c] = '.'
        
        # how many removed in this iteration
        total_removed_count += len(to_remove)
    return total_removed_count


with open("./day4/input.txt", 'r') as f:
    lines = f.readlines()
    grid_data = [list(line.strip()) for line in lines]

result = solve_iterative(grid_data)
print(result)