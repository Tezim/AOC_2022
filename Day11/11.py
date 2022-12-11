filename = "input.txt"

with open(filename,'r') as f:
    content = f.read().split("\n\n")

# monkey : 0...
# list : ----
# op : .....
# test : ....
# true : ....
# false : .....
monkeys = []
round = 0

lcm = 1

for i in range(len(content)):
    tmp = content[i].split("\n")
    monkey = dict()
    monkey['id'] = int(tmp[0].split()[1].split(":")[0])
    monkey['items'] = [int(s) for s in tmp[1].split(":")[1].split(',')]
    monkey['op'] = tmp[2].split("=")[1]
    monkey['mod'] = int(tmp[3].split("by")[1])
    monkey['True'] = int(tmp[4].split("monkey")[1])
    monkey['False'] = int(tmp[5].split("monkey")[1])
    monkey['counter'] = 0
    lcm *= monkey['mod']
    monkeys.append(monkey)


while round < 10000:
    for m in monkeys:
        for item in m['items']:
            op = m['op'].split()
            new = 0
            if op[2] == "old":
                by = item
            else:
                by = int(op[2])
            if op[1] == "+":
                new = item + by
            elif op[1] == "*":
                new = item * by
            #new = new // 3
            new = new % lcm  #wau
            monkeys[m[str(new%m['mod'] == 0)]]['items'].append(new)
            m['counter'] += 1
        m['items'] = []
    round += 1

counts = []

for m in monkeys:
    counts.append(m['counter'])
counts.sort(reverse=True)
print(counts[0]*counts[1])


