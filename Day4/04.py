
filename = "input.txt"

with open(filename,'r') as f:
    content = f.readlines()


counter = 0
counter2 = 0

for line in content:

    sec = line.strip().split(',')
    elf1 = sec[0].split('-')
    elf2 = sec[1].split('-')
    if int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]):
        counter += 1
        counter2 += 1
    elif int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
        counter +=1
        counter2 += 1
    elif int(elf1[0]) <= int(elf2[0]) <= int(elf1[1]) <= int(elf2[1]):
        counter2 += 1
    elif int(elf2[0]) <= int(elf1[0]) <= int(elf2[1]) <= int(elf1[1]):
        counter2 += 1


print(counter)
print(counter2)
