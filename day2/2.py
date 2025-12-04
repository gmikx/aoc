with open("./day2/input.txt") as f:
    ranges_str = f.read().strip()

raw_ranges = sorted(tuple(map(int, r.split("-"))) for r in ranges_str.split(","))

merged_ranges = []
curr_start, curr_end = raw_ranges[0]
for next_start, next_end in raw_ranges[1:]:
    if next_start <= curr_end + 1:
        curr_end = max(curr_end, next_end)
    else:
        merged_ranges.append((curr_start, curr_end))
        curr_start, curr_end = next_start, next_end
merged_ranges.append((curr_start, curr_end))

global_max = merged_ranges[-1][1]
max_digits = len(str(global_max))

def is_periodic(n):
    s = str(n)
    l = len(s)
    for i in range(1, l // 2 + 1):
        if l % i == 0 and s[:i] * (l // i) == s:
            return True
    return False

total = 0

for L in range(1, max_digits // 2 + 1):
    min_seed = 10**(L - 1)
    max_seed = 10**L - 1
    
    k = 2
    while True:
        multiplier = (10**(k * L) - 1) // (10**L - 1)
        
        min_val = min_seed * multiplier
        max_val = max_seed * multiplier
        
        if min_val > global_max:
            break
        
        for r_start, r_end in merged_ranges:
            if r_end < min_val:
                continue
            if r_start > max_val:
                break
            
            s_min = (r_start + multiplier - 1) // multiplier
            s_max = r_end // multiplier
            
            start_s = max(min_seed, s_min)
            end_s = min(max_seed, s_max)
            
            if start_s <= end_s:
                for s in range(start_s, end_s + 1):
                    if not is_periodic(s):
                        total += s * multiplier
        
        k += 1

print(total)