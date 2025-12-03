def get_val(initial:int, operation:str)->int:
    magnitude = int(operation[1:])
    if operation[0]=="L":
        magnitude *= -1

    return (initial+magnitude)%100


val=50
count=0

with open("./day1/input.txt",'r') as f:
    for line in f:
        print(f"{val} + {line} -> ", sep="")

        val = get_val(val, line.strip())
        if val==0: count +=1

        print(val, )

print(count)