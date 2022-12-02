filename = "input.txt"


with open(filename,'r') as f:
    content = f.readlines()

points = 0
pointsb = 0

for rnd in content:
    tmp = rnd.split()
    if tmp[0] == 'A':
        if tmp[1] == 'X':
            points += 4
            pointsb += 3
        if tmp[1] == 'Y':
            points += 8
            pointsb += 4
        if tmp[1] == 'Z':
            points += 3
            pointsb += 8
    elif tmp[0] == 'B':
        if tmp[1] == 'X':
            points += 1
            pointsb += 1
        if tmp[1] == 'Y':
            points += 5
            pointsb += 5
        if tmp[1] == 'Z':
            points += 9
            pointsb += 9
    elif tmp[0] == 'C':
        if tmp[1] == 'X':
            points += 7
            pointsb += 2
        if tmp[1] == 'Y':
            points += 2
            pointsb += 6
        if tmp[1] == 'Z':
            points += 6
            pointsb += 7

print(points)
print(pointsb)
