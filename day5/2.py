counter=0

with open("./day5/input.txt",'r') as f:
    line = f.readline().strip()
    while (line):
        line_num, line_num2 = map(int,line.split("-"))
        counter += line_num2 - line_num + 1
        line = f.readline().strip()

print(counter)