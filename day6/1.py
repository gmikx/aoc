import numpy as np

def multiply(iterable:list):
    result = 1
    for i in iterable:
        result *= i
    return result

def column(list:list, row:int):
    return [i[row] for i in list]


f = open("./day6/input.txt", 'r')
input = f.readlines()
f.close()
data=[]
operations=[]
calculations=[]

for i, line in enumerate(input):
    data_ = line.split()
    if i!=len(input)-1:
        data_ = list(map(int, data_))
        data.append(data_)
    if i==len(input)-1:
        operations = data_

# data_np = np.array(data)
# print(data)
# print(data[4][1:10])
for i in range(len(data[0])):
    if operations[i]=="+":
        calculations.append(sum(column(data, i)))
        print("+,", i,"elementy:", column(data, i), ":", sum(column(data, i)))
    elif operations[i]=="*":
        calculations.append(multiply(column(data, i)))
        print("*, ", i, ":", multiply(column(data, i)))

print(sum(calculations))