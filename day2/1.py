f = open("./day2/input.txt",'r')
ranges = f.readline()
f.close()

ranges = ranges.split(",")
ranges = [tuple(map(int, i.split("-"))) for i in ranges]

def is_silly_id(id: str)->bool:
    if len(id)%2 == 1:
        return False
    if id[:len(id)//2]==id[len(id)//2:]:
        return True

id_sum=0

for range_ in ranges:
    for i in range(range_[0], range_[1]+1):
        if is_silly_id(str(i)):
            id_sum+=i

print(id_sum)