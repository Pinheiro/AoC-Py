import graphtheory
import itertools
import re

fname = '2015-09.txt'

def solve(f):
    p = [i.split(',') for i in re.compile(r'(.+) to (.+) = (.+)').sub(r'\1,\2,\3', f).splitlines()]
    g = graphtheory.Graph()
    for i in range(len(p)):
        g.addNode(p[i][0])
        g.addNode(p[i][1])
        g.addEdge(p[i][0], p[i][1], int(p[i][2]))
    # create a list of routes with all nodes on each route
    r = list(itertools.permutations(g.nodes))
    # calculate the distance (weight) for each route
    d = [0] * len(r)
    for i in range(len(r)):
        for j in range(len(r[i]) - 1):
            d[i] += g.getWeight(r[i][j], r[i][j + 1])
    # return distances (weights) for routes with all nodes
    return d

assert min(solve(open('2015-09-0.txt').read())) == 605

print()
print("event 2015 day 9 part 1 answer: ", min(solve(open(fname).read())))

assert max(solve(open('2015-09-0.txt').read())) == 982

print()
print("event 2015 day 9 part 2 answer: ", max(solve(open(fname).read())))

