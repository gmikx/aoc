def findJoltage(input_str:str, batteries:int)->str:
    if len(input_str) == batteries:
        return input_str

    largest_idx = 0
    largest = "0"

    for i in range(len(input_str) - batteries + 1):
        c = input_str[i]
        if largest<c:
            largest = c
            largest_idx = i

    remaining_input = input_str[largest_idx+1:]
    if batteries>1:
        return largest + findJoltage(remaining_input, batteries-1)
    else: return largest

with open("./day3/input.txt",'r') as f:
    solution=0
    for line in f:
        partial_sol=int(findJoltage(line.strip(), 2))
        solution += partial_sol
        print(partial_sol)
    print(solution)

