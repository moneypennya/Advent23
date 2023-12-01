with open('input.txt') as f:
    lines = f.read().splitlines()
summ = 0
for i in range(len(lines)):
    for x in range(len(lines[i])):
        if lines[i][x].isnumeric():
            first = lines[i][x]
            break
    for y in reversed(range(len(lines[i]))):
        if lines[i][y].isnumeric():
            last = lines[i][y]
            break
    summ += int(first + last)
print(summ)
         