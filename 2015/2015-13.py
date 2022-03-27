from itertools import permutations
import re

def happiness(planning, myself):
    
    p = planning
    p = p.replace("gain ", "")
    p = p.replace("lose ", "-")
    p = re.findall(r'(\w+) would (-?\d+) happiness units by sitting next to (\w+)', p)
    p = [list(x) for x in p]
    
    attendees = set()
    if myself:
        attendees.add('myself')
    
    seatings = dict()
    
    for i in range(len(p)):
        attendees.add(p[i][0])
        seatings[(p[i][0], p[i][2])] = int(p[i][1])
        seatings[(p[i][0], 'myself')] = 0
        seatings[('myself', p[i][0])] = 0
    
    arrngmnts = list(permutations(attendees))
    
    happiness = [0] * len(arrngmnts)
    
    for a in range(len(arrngmnts)):
        for p in range(len(arrngmnts[a])):
            happiness[a] += seatings[(arrngmnts[a][p], arrngmnts[a][p - 1])] 
            happiness[a] += seatings[(arrngmnts[a][p], arrngmnts[a][(p+1)%(len(arrngmnts[a]))])]
    
    return happiness

plan = '''Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
'''

assert max(happiness(plan, False)) == 330
fname = '2015-13.txt'
print()
print("event 2015 day 13 part 1 answer: ", max(happiness(open(fname).read(), False)))
print()
print("event 2015 day 13 part 2 answer: ", max(happiness(open(fname).read(), True)))