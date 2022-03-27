import re

fname = '2015-05.txt'

def IsNice(s, mode):
    p = [True]*5
    if mode == 1:
        p[0] = len(re.findall("[aeiou]", s)) > 2
        p[1] = len(re.findall("(\w)\\1", s)) > 0
        p[2] = len(re.findall("ab|cd|pq|xy", s)) == 0
    elif mode == 2:
        p[3] = len(re.findall("(\w\w).*\\1", s)) > 0
        p[4] = len(re.findall("(\w).\\1", s)) > 0
    return all(p)

assert IsNice("ugknbfddgicrmopn", 1)
assert IsNice("aaa", 1)
assert ~IsNice("jchzalrnumimnmhp", 1)
assert ~IsNice("haegwjzuvuyypxyu", 1)
assert ~IsNice("dvszwmarrgswjxmb", 1)

inp = [line.strip() for line in open(fname).readlines()]

print()
print("event 2015 day 5 part 1 answer: ", sum([IsNice(s, 1) for s in inp]))

assert IsNice("qjhvhtzxzqqjkmpb", 2)
assert IsNice("xxyxx", 2)
assert ~IsNice("uurcxstgmygtbstg", 2)
assert ~IsNice("ieodomkazucvgmuy", 2)

print()
print("event 2015 day 5 part 2 answer: ", sum([IsNice(s, 2) for s in inp]))