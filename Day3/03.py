from math import floor

filename = "input.txt"


def eval_char(s):
    for c in s:
        if c.islower():
            return ord(c) - 96
        elif c.isupper():
            return ord(c) - 38


def eval2(input):
    intersec = ''.join(set(input[0]).intersection(input[1],input[2]))
    return eval_char(intersec)


with open(filename,'r') as f:
    content = f.readlines()

sum = 0
sum2 = 0
counter = 0
group = []
for line in content:
    if counter < 3:
        group.append(line)
        counter += 1
        if counter == 3:
            counter = 0
            sum2 += eval2(group)
            group = []

    first = slice(0, floor(len(line)/2))
    second = slice(floor(len(line)/2), len(line)-1)
    intersec = ''.join(set(line[first]).intersection(line[second]))
    sum += eval_char(intersec)

print(sum)
print(sum2)

