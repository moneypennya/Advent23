with open('input1.txt') as f:
    lines = f.read().splitlines()
    summ = 0
for i in range(len(lines)):
    holder = lines[i].split(":")[1]
    gamenum = int(lines[i].split(":")[0].replace("Game ", ""))
    lines[i] = holder.replace(" ", "")
    games = lines[i].split(";")
    bad = 0
    for z in range(len(games)):
        for y in range(len(games[z])):
            if(games[z][y].isnumeric() and games[z][y+1].isnumeric()):
                color = games[z][y:y+3]
                number = int(color[0] + color[1])
                if color[2] == "r":
                    if number > 12:
                        bad  = 1
                        break
                elif color[2] == "b":
                    if number > 14:
                        bad  = 1
                        break
                elif color[2] == "g":
                    if number > 13:
                        bad  = 1
                        break
    if bad == 0:
        summ = summ + gamenum        
print(summ)