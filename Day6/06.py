filename = "input.txt"
#filename = "test.txt"

with open(filename,'r') as f:
    content = f.read().rstrip()

for i in range(len(content)-13):  #3
    tmp = []
    for j in range(14):  #4
        if content[i+j] not in tmp:
            tmp.append(content[i+j])
        else:
            tmp = []
            break
    if len(tmp) == 14:  #4
        print(i+j + 1)
        break


