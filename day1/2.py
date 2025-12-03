def get_val(initial:int, operation:str)->int:
    click=0
    magnitude = int(operation[1:])

    if operation[0]=="L":
        magnitude *= -1
    
    click=abs((initial+magnitude))//100

    if (initial+magnitude < 0 and initial!=0): click+=1
    if (initial+magnitude == 0 and magnitude != 0): click=1

    print(f"{initial} + {operation} -> {initial+magnitude} ({(initial+magnitude)%100}), click = {click}")

    return (initial+magnitude)%100, click


val=50
count=0

with open("./day1/input.txt",'r') as f:
    for line in f:
        val, click = get_val(val, line.strip())
        count += click

print(count)