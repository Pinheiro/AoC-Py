from itertools import combinations

fname = '2015-02.txt'

d = [p.split('x') for p in open(fname).read().splitlines()]
d = [[int(n) for n in p] for p in d]
d = [list(combinations(p, 2)) for p in d]
d = [[s[0]*s[1] for s in p] for p in d]
d = [2*sum(p)+min(p) for p in d]

print()
print("event 2015 day 2 part 1 answer: ", sum(d))

d = [p.split('x') for p in open(fname).read().splitlines()]
d = [sorted([int(n) for n in p]) for p in d]
d = [2*(p[0]+p[1])+p[0]*p[1]*p[2] for p in d]

print()
print("event 2015 day 2 part 2 answer: ", sum(d))