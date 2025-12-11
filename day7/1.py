def findOccurrences(string:str, ch) -> list[int]:
    return [i for i, letter in enumerate(string) if letter == ch]

with open("./day7/input.txt") as f:
    start_index = f.readline().find('S')
    count_splits = 0
    beams = [start_index]
    for line in f:
        splitters = findOccurrences(line, "^")
        print(line)
        # new_beams=[]
        for i in splitters:
            if i in beams:
                count_splits += 1
                beams.extend([i-1, i+1])
                while(i in beams):
                    beams.remove(i)

        # beams = set(new_beams)

print(count_splits)