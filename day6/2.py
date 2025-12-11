def multiply(iterable:list):
    result = 1
    for i in iterable:
        result *= i
    return result

def column(list:list, row:int):
    return [i[row] for i in list]

def isempty(list:list):
    for i in list:
        if i!=" ":
            return False
    return True

f = open("./day6/input.txt", 'r')
input = f.readlines()
f.close()
data=input[:-1]
data_processed=[]
operations=input[-1].strip().split()
calculations=[]
temp_numbers=[]
which_operation=0
for i in data:
    data_processed.append(i[:-1])

print(data_processed)

for i in range(len(data_processed[0])):
    temp_column = column(data_processed, i)
    if isempty(temp_column):
        if operations[which_operation]=="+":
            calculations.append(sum(temp_numbers))
            print("+,", i,"elementy:", temp_numbers, ":", sum(temp_numbers))
        elif operations[which_operation]=="*":
            calculations.append(multiply(temp_numbers))
            print("*, ", i, "elementy:", temp_numbers,  ":", multiply(temp_numbers))
        which_operation+=1
        temp_numbers=[]
    else: 
        temp_numbers.append(int("".join(temp_column)))
if operations[which_operation]=="+":
    calculations.append(sum(temp_numbers))
    print("+,", i,"elementy:", temp_numbers, ":", sum(temp_numbers))
elif operations[which_operation]=="*":
    calculations.append(multiply(temp_numbers))
    print("*, ", i, "elementy:", temp_numbers,  ":", multiply(temp_numbers))

print(sum(calculations))