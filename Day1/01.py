filename = "input.txt"


with open(filename,'r') as f:
    content = f.readlines()

top = []
min_in_top = 0
tmp = 0
cals = 0

for line in content:
    if line == '\n':
        if tmp > cals:
            cals = tmp
        top.append(tmp)
        tmp = 0
    else:
        tmp += int(line.strip())

top.sort(reverse = True)

print((top[0] + top[1] + top[2]))
print(cals)



