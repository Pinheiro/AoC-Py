import re

fname = '2015-06.txt'

def execute(instruction):
    for x in range(int(instruction[1]), int(instruction[3]) + 1):
        for y in range(int(instruction[2]), int(instruction[4]) + 1):
            if instruction[0] == 'turn on':
                grid1[x][y] = 1
                grid2[x][y] += 1
            if instruction[0] == 'turn off':
                grid1[x][y] = 0
                grid2[x][y] -= 1
                if grid2[x][y] < 0:
                    grid2[x][y] = 0
            if instruction[0] == 'toggle':
                if grid1[x][y] == 0:
                    grid1[x][y] = 1
                else:
                    grid1[x][y] = 0
                grid2[x][y] += 2

pattern = re.compile(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)')
instructions = pattern.sub(r'\1,\2,\3,\4,\5', open(fname).read()).splitlines()
instructions = [x.split(',') for x in instructions]
grid1 = [[0 for _ in range(1000)] for _ in range(1000)]
grid2 = [[0 for _ in range(1000)] for _ in range(1000)]
for instruction in instructions:
    execute(instruction)

print()
print("event 2015 day 6 part 1 answer: ", sum([sum(i) for i in grid1]))

print()
print("event 2015 day 6 part 2 answer: ", sum([sum(i) for i in grid2]))