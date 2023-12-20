import sys
ret = 0
for line in sys.stdin:
    strlist = line.strip().split(' ')
    list = []
    for elem in strlist:
        list.append(int(elem))
    subLists = [list]
    keepGoing = True
    while keepGoing:
        subList = []
        prev = subLists[-1][0]
        keepGoing = False
        for elem in subLists[-1][1:]:
            res = elem - prev
            subList.append(res)
            prev = elem
            if (res != 0):
                keepGoing = True
        subLists.append(subList)    

    subLists.reverse()
    subLists[0].append(0)
    for index, subList in enumerate(subLists[1:]):
        a = subList[0]
        b = subLists[index][0]
        subList.insert(0,a-b)
    # print(subLists)
    ret+=subLists[-1][0]
print(ret)