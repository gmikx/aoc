from functools import cache
def findOccurrences(string:str, ch) -> list[int]:
    return [i for i, letter in enumerate(string) if letter == ch]

@cache
def followRay(start:int, row:int):
    if row >= len(input_text):
        return 1
    current_char = input_text[row][start]
    if current_char == "^":
        return followRay(start-1, row+1) + followRay(start+1, row+1)
    else: 
        return followRay(start, row+1)


f = open("./day7/input.txt")
input_text = f.readlines()
f.close()

start_index = input_text[0].find('S')

number = followRay(start_index, 1)

print(number)