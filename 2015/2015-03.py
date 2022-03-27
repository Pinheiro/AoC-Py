
fname = '2015-03.txt'

def move(x, y, m, h):
    r1, r2 = x, y
    if m == "^": r1 += 1
    if m == "v": r1 -= 1
    if m == ">": r2 += 1
    if m == "<": r2 -= 1
    if (r1, r2) in h.keys():
        h[(r1, r2)] += 1
    else:
        h[(r1, r2)] = 1
    return r1, r2
    
d = open(fname).read()
x, y = 0, 0
houses = dict()
houses[(x, y)] = 1
i = 0
while True:
    x, y = move(x, y, d[i], houses)
    i += 1
    if i == len(d):
        break
print()
print("event 2015 day 3 part 1 answer: ", len(houses))

d = open(fname).read()
x0, y0 = 0, 0
x1, y1 = 0, 0
houses = dict()
houses[(x0, y0)] = 1
houses[(x1, y1)] += 1
i = 0
while True:
    x0, y0 = move(x0, y0, d[i], houses)
    i += 1
    if i == len(d):
        break
    x1, y1 = move(x1, y1, d[i], houses)
    i += 1
    if i == len(d):
        break
print()
print("event 2015 day 3 part 2 answer: ", len(houses))