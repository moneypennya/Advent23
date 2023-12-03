with open('test.txt') as f:
    lines = f.read().splitlines()
    summ = 0
for i in range(len(lines)):
    holder = lines[i].split(":")[1]
    gamenum = int(lines[i].split(":")[0].replace("Game ", ""))
    lines[i] = holder.replace(" ", "")
    games = lines[i].split(";")
    redmax, bluemax, greenmax = (0,0,0)
    for z in range(len(games)):
        for y in range(len(games[z])):
            if(games[z][y].isnumeric() and games[z][y+1].isnumeric()):
                color = games[z][y:y+3]
                number = int(color[0] + color[1])
                if color[2] == "r":
                    if number > redmax:
                        redmax = number
                elif color[2] == "b":
                    if number > bluemax:
                        bluemax = number
                elif color[2] == "g":
                    if number > greenmax:
                        greenmax = number
            elif (games[z][y].isnumeric()):
                color = games[z][y:y+2]
                number = int(color[0])
                if color[1] == "r":
                    if number > redmax:
                        redmax = number
                elif color[1] == "b":
                    if number > bluemax:
                        bluemax = number
                elif color[1] == "g":
                    if number > greenmax:
                        greenmax = number  
    power = redmax * bluemax * greenmax
    summ = summ + power       
print(summ)