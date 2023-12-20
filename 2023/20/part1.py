import sys

flipflops = {}
conjunctions = {}

adj = {}
rAdj = {}

for line in sys.stdin:
    newLine = line.strip().split('->')
    module = newLine[0].strip()
    dests = newLine[1].replace(' ','').split(',')
    type = module[0] if module[0] == '%' or module[0] == '&' else 'b'
    module = module.replace('%', '')
    module = module.replace('&', '')

    adj[module] = []
    for dest in dests:
        adj[module].append(dest)
        if (dest not in rAdj):
            rAdj[dest] = []
        rAdj[dest].append(module)
    if (type == '%'):
        flipflops[module] = 0
    elif  (type == '&'):
        conjunctions[module] = {}

for conjunction in conjunctions:
    res = {}
    for mod in rAdj[conjunction]:
        res[mod] = 0
    conjunctions[conjunction] = res
low = 0
high = 0
iniNode = "broadcaster"
for i in range(0,1000):
    # press button
    low+=1
    queue = []
    for n in adj[iniNode]:
        low+=1
        queue.append([n, 0, iniNode])
    while len(queue) > 0:
        next = queue.pop(0)
        mod = next[0]
        signal = next[1]
        prev = next[2]
        pulse = 0
        if (mod in flipflops):
            if (signal == 0):
                pulse = 0
                if (flipflops[mod] == 0):
                    pulse = 1
                    flipflops[mod] = 1
                else:
                    pulse = 0
                    flipflops[mod] = 0
                for n in adj[mod]:
                    if (pulse == 0):
                        low+=1
                    else:
                        high+=1
                    queue.append([n, pulse, mod])
        elif (mod in conjunctions):
            conjunctions[mod][prev] = signal
            pulse = 0
            for input in conjunctions[mod]:
                if (conjunctions[mod][input] == 0):
                    pulse = 1
            for n in adj[mod]:
                if (pulse == 0):
                    low+=1
                else:
                    high+=1
                queue.append([n, pulse, mod])

print(low * high)
for elem in rAdj:
    print (elem)
    # Flip-flop modules (prefix %) 
    # are either on or off; they are initially off. 
    # If a flip-flop module receives a high pulse, it is ignored and nothing happens. 
    # However, if a flip-flop module receives a low pulse, it flips between on and off. 
    # If it was off, it turns on and sends a high pulse. 
    # If it was on, it turns off and sends a low pulse.

    # Conjunction modules (prefix &) 
    # remember the type of the most recent pulse received from each of their connected input modules; 
    # they initially default to remembering a low pulse for each input. 
    # When a pulse is received, the conjunction module 
    # first updates its memory for that input. 
    # Then, if it remembers high pulses for all inputs, it sends a low pulse;
    # otherwise, it sends a high pulse.
