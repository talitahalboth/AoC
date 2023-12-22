line = input().strip()
list = line.split(',')
res = 0
for rule in list:
    cur = int(0)
    for c in rule:
        ascii = ord(c)
        cur+=ascii
        cur*=17
        cur%=256
    res+=cur

print(res)