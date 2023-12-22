line = input().strip()
list = line.split(',')
res = 0

def calculateHash(label):
    cur = int(0)
    for c in label:
        ascii = ord(c)
        cur+=ascii
        cur*=17
        cur%=256
    return cur
    
boxes = {}
for i in range(0, 256):
    boxes[i] = []
def removeLabelFromBox(label, index):
    for ix, box in enumerate(boxes[index]):
                if box[0] == label:
                    boxes[index].pop(ix)
                    break
def updateFocalLength(label, focalLegnth, index):
    for ix, box in enumerate(boxes[index]):
                if box[0] == label:
                    box[1] = focalLegnth
                    return
    boxes[index].append([label, focalLegnth])

for rule in list:
    if ('-' in rule):
        label = rule[:rule.find('-')]
        index = calculateHash(label)
        removeLabelFromBox(label, index)
    else:
        label = rule[:rule.find('=')]
        focalLegnth = rule[rule.find('=')+1:]
        box = calculateHash(label)
        # boxes[box].append([label, focalLegnth])
        updateFocalLength(label, focalLegnth, box)
    # print(rule)
res = 0
for box in boxes:
    for ix, content in enumerate(boxes[box]):
        a = 1 + int(box)
        b = ix+1
        c = int(content[1])
        res+=a*b*c
    
print(res)