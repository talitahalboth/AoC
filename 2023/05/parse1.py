seedsInfo = input()
seedsList = seedsInfo.split(' ')[1:]
print(len(seedsList))
for seed in seedsList:
    print(seed, end=' ')
input()

for i in range(0,7):
    inputLine = input()
    inputLineList = []
    while (len(inputLine) > 0):
        inputLineList.append(inputLine.split(' '))
        try:
            inputLine = input()
        except:
            break 


    inputLineList = inputLineList[1:]
    print(len(inputLineList))
    for elem in inputLineList:
        for item in elem:
            print(item, end=' ')
        print()