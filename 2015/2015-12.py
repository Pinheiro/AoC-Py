import re

fname = '2015-12.txt'

print()
r1 = sum([int(n) for n in re.findall(r'-?\d+', open(fname).read())])
print("event 2015 day 11 part 1 answer: ", r1)

import json

def jsum(js):
    if isinstance(js, dict) and not 'red' in js.values():
        return sum(map(jsum, js.values()))
    elif isinstance(js, list):
        return sum(map(jsum, js))
    elif isinstance(js, int):
        return js
    else:
        return 0

print()
print("event 2015 day 11 part 2 answer: ", jsum(json.load(open(fname))))