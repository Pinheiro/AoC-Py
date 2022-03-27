fname = '2015-08.txt'

def total(file):
    return sum([len(s) - len(eval(s)) for s in open(file).read().splitlines()])

assert total('2015-08-0.txt') == 12

print()
print("event 2015 day 8 part 1 answer: ", total(fname))

def newtotal(file):
    return sum([2 + s.count('\\') + s.count('"') for s in open(file).read().splitlines()])

assert newtotal('2015-08-0.txt') == 19

print()
print("event 2015 day 8 part 2 answer: ", newtotal(fname))
