import re

def lookandsay(look):
    parts = [part.group(0) for part in re.finditer(r"(\d)\1*", look)]
    say = [str(len(part)) + part[0] for part in parts]
    return ''.join(say)

assert lookandsay('1') == '11'
assert lookandsay('11') == '21'
assert lookandsay('21') == '1211'
assert lookandsay('1211') == '111221'
assert lookandsay('111221') == '312211'

def solve(pi, n):
    r = pi
    for i in range(n):
        r = lookandsay(r)
    return r

print()
r1 = solve('1113122113', 40)
print("event 2015 day 10 part 1 answer: ", len(r1))

print()
r2 = solve(r1, 10)
print("event 2015 day 10 part 2 answer: ", len(r2))