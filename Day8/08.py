filename = "input.txt"
#filename = "test.txt"


def get_score(actual,list):
    for k in range(len(list)):
        if list[k] >= actual:
            return k + 1
    return len(list)


with open(filename,'r') as f:
    content = f.readlines()

counter = 0
count = 0
height = len(content)
width = len(content[0].strip())
biggest_score = 0;


for line in content:
    if counter != 0 and counter != height-1:
        line = line.strip()
        for i in range(1, len(line)-1):
            actual = int(line[i])
            left = line[0:i]
            scenic_score = 1

            right = line[i+1:]
            top = []
            down = []
            for t in range(counter):
                top.append(content[t][i])
            for t in range(1,height-counter):
                down.append(content[counter+t][i])
            right = [int(x) for x in right]
            left = [int(x) for x in left]
            top = [int(x) for x in top]
            down = [int(x) for x in down]

            rb = True
            lb = True
            tb = True
            db = True

            if any(x >= actual for x in right):
                rb = False
            if any(x >= actual for x in left):
                lb = False
            if any(x >= actual for x in top):
                tb = False
            if any(x >= actual for x in down):
                db = False

            if tb or db or lb or rb:
                count += 1
            if len(left) > 1:
                left.reverse()
            if len(top) > 1:
                top.reverse()
            scenic_score *= get_score(actual, right)
            scenic_score *= get_score(actual, left)
            scenic_score *= get_score(actual, top)
            scenic_score *= get_score(actual, down)

            if scenic_score > biggest_score:
                biggest_score = scenic_score

    counter += 1

outline = (height*2 + width*2)-4
print(count + outline)
print(biggest_score)



