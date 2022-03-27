import re

fname = '2015-01.txt'

def floor(puzzle):
    return len(re.findall("[(]", puzzle)) - len(re.findall("[)]", puzzle))

f = open(fname).read()

print()
print("event 2015 day 1 part 1 answer: ", floor(f))

i = -1
while True:
    i += 1
    if floor(f[0:i]) == -1:
        break

print()
print("event 2015 day 1 part 1 answer: ", i)