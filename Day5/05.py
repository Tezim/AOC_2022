import re
from collections import deque

filename = "input.txt"

with open(filename,'r') as f:
    content = f.readlines()

content = ''.join(content).split("\n\n")
stack = [
    ['R','N','P','G'],
    ['T','J','B','L','C','S','V','H'],
    ['T','D','B','M','N','L'],
    ['R','V','P','S','B'],
    ['G','C','Q','S','W','M','V','H'], # 30 minutes of debug for one wrong letter
    ['W','Q','S','C','D','B','J'],
    ['F','Q','L'],
    ['W','M','H','T','D','L','F','V'],
    ['L','P','B','V','M','J','F']
]


# stack = [
#     ['Z','N'],
#     ['M','C','D'],
#     ['p']
# ]
def move(n,fr,to):
    tmp = stack[fr - 1][-n:]
    del stack[fr-1][-n:]
    #* uncoment for part 1
    #tmp.reverse()
    stack[to-1].append(tmp)
    stack[to - 1] = [item for sublist in stack[to-1] for item in sublist]


for instruction in content[1].split('\n'):
    instr = instruction.split(" ")
    num = int(instr[1])
    fr = int(instr[3])
    to = int(instr[5])
    move(num,fr,to)


out = []
for i in range(len(stack)):
    out.append( stack[i][len(stack[i])-1])
print(''.join(out))