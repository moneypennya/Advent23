with open('input2.txt') as f:
    lines = f.read().splitlines()
summ = 0
nums = {1: "one", 2: "two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    
for i in range(len(lines)):
    firstword = ""
    secondword = ""
    for x in range(len(lines[i])):
        if lines[i][x].isnumeric():
            first = lines[i][x]
            break
        else:
            breakagain = 0
            firstword = firstword + lines[i][x]
            for key in nums:
                if firstword.find(nums[key]) != -1:
                    first = str(key)
                    breakagain=1
                    break
            if breakagain == 1:
                break
    for y in reversed(range(len(lines[i]))):
        if lines[i][y].isnumeric():
            last = lines[i][y]
            break
        else:
            breakagain = 0
            secondword = lines[i][y] + secondword
            for key in nums:
                if secondword.find(nums[key]) != -1:
                    last = str(key)
                    breakagain=1
                    break
            if breakagain == 1:
                break
    summ += int(first + last)
    print(int(first+last))
print(summ)