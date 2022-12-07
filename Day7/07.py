filename = "input.txt"

with open(filename,'r') as f:
    content = f.readlines()


last_dir = 0
last_dir_name = []
sums = {"/":0}
offset = 0
last_dir_name.append("/")
for l in range(len(content)):
        command = content[l + offset].strip().split()
        if command[0] == "$":
            #subroutine
            if command[1] == "cd":
                if command[2] ==  "..": #step out
                    last_dir_name.pop()
                elif command[2] == "/": #change dir
                    last_dir_name = ["/"]
                else:  # move in
                    last_dir_name.append(command[2])
        elif command[0] == 'dir':
             sums["".join(last_dir_name) + command[1]] = 0
        else:
             sums["".join(last_dir_name)] += int(command[0])
             for i in range(1, len(last_dir_name)):
                 for key, value in sums.items():
                     if key == "".join(last_dir_name[:-i]):
                         sums[key] = value + int(command[0])


result = 0
for key, value in sums.items():
    if value < 100000:
        result += value


SIZE = 70000000
curr_size = sums["/"]

free = 30000000 - abs(SIZE - curr_size)
dirs = []

for key,value in sums.items():
    if value >= free:
        dirs.append(value)
dirs.sort()

print(dirs[0])
print(result)
