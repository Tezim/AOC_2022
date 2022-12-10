filename = "input.txt"

with open(filename, 'r') as f:
    content = f.readlines()

cycle = 0
line_counter = 0
target = 20
signal_strength = 0
crt = 1
sum_ = 1
l = "#"
loop = 1
for line in content:
    if line.split()[0] == "noop":
        cycle += 1
        loop = 1
    else:
        cycle += 2
        loop = 2
    line_counter += 1
    for i in range(loop):
        if sum_ == (crt -2 )% 40 or sum_ == (crt-1)%40 or sum_ == crt%40:
            l+="#"
        else:
            l += "."
        crt +=1
        if (len(l) -1 )%40 == 0:
            l += "#"
            print(l)
            l = "#"

    if cycle >= target:
        signal_strength += (sum_ * target)
        target += 40
    if line.split()[0] == "addx":
        sum_ += int(float(line.split()[1]))
    # if cycle >= target:
    #     sum_ = 1
    #     for i in range(line_counter-1):
    #         if content[i].split()[0] == "addx":
    #             sum_ += int(float(content[i].split()[1]))
    #     signal_strength += (sum_ * target)
    #     target += 40
    #
print(signal_strength)
