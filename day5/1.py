def is_included(element, list):
    for i in range(len(list)):
        if list[i][1] >= element >= list[i][0]:
            return 1
    return 0

ranges = []
counter = 0

with open("./day5/input.txt",'r') as f:
    line = f.readline().strip()
    while (line):
        line_num, line_num2 = map(int,line.split("-"))
        ranges.append([line_num, line_num2])
        line = f.readline().strip()

    line=f.readline().strip()
    while(line):
        if is_included(int(line), ranges):
            counter+=1
        line = f.readline().strip()


print(counter)