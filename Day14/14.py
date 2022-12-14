filename = "input.txt"
#filename = "test.txt"

with open(filename,'r') as f:
    content = f.readlines()

Y = 0
for line in content:
    line = line.split('->')
    for i in range(len(line)-1):
        y1 = line[i].strip().split(',')[1]
        y1 = int(y1)
        if y1 > Y:
            Y = y1

Y += 2
map_ = [["." for i in range(1000)] for j in range(200)]
for i in range(1000):
    map_[Y][i] = '#'


for line in content:
    line = line.split('->')
    for i in range(len(line)-1):
        x1, y1 = line[i].strip().split(',')
        x2, y2 = line[i + 1].strip().split(',')
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        if x1 == x2:
            if y1 < y2:
                start = y1
                end = y2
            elif y1 > y2:
                start = y2
                end = y1
            for k in range(start, end + 1):
                map_[k][x1] = '#'
        elif y1 == y2:
            if x1 < x2:
                start = x1
                end = x2
            elif x1 > x2:
                start = x2
                end = x1
            for k in range(start, end + 1):
                map_[y1][k] = '#'

counter = 0
void = False
while not void:
    sandX = 500
    sandY = 0
    fly = True
    if counter == 23:
        print()
    try:
        while fly:
            if map_[sandY + 1][sandX] != '#' and map_[sandY + 1][sandX] != 'o':
                sandY += 1
            else:
                if map_[sandY + 1][sandX - 1] != '#' and map_[sandY + 1][sandX - 1] != 'o':
                    sandX -=1
                    sandY +=1
                elif map_[sandY + 1][sandX + 1] != '#' and map_[sandY + 1][sandX + 1] != 'o':
                    sandX += 1
                    sandY += 1
                else:
                    map_[sandY][sandX] = 'o'
                    fly = False
                    counter += 1
            #+
            if sandY == 0 and sandX == 500:
                void = True
                print('Part 2')
            #+   
    except: #not the best option but it works :D
        void = True

print(counter)