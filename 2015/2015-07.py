import re

fname = '2015-07.txt'

def getWire(file, b=None):
    inp = open(file, 'r').read()
    for r in (("AND", "&"), ("OR", "|"), ("LSHIFT", "<<"), ("RSHIFT", ">>"), ("NOT", "~")):
        inp = inp.replace(*r)
    if b != None:
        inp = inp.replace('1674 -> b', str(b) + ' -> b')
    instruc = [i.split(',') for i in re.compile(r'(.*) -> ([a-z]+)').sub(r' \1 ,\2', inp).splitlines()]
    wires = dict()
    i = 0
    while True:
        if instruc[i][0].isdigit():
            wires[instruc[i][1]] = int(instruc[i][0])
            instruc.pop(i)
        else:
            if len(re.findall(r'[a-z]', instruc[i][0])) == 0:
                if len(re.findall(r'~', instruc[i][0])) == 0:
                    instruc[i][0] = str(eval(instruc[i][0]))
                else:
                    instruc[i][0] = str(eval(instruc[i][0]) + (1 << 16))
            else:
                for wire in wires:
                    if instruc[i][0].find(wire) != -1:
                        instruc[i][0] = instruc[i][0].replace(' ' + wire + ' ', str(wires[wire]))
            i += 1
        if len(instruc) == 0:
            break
        if i == len(instruc):
            i = 0
    return wires['a']

a = getWire(fname)

print()
print("event 2015 day 7 part 1 answer: ", a)

print()
print("event 2015 day 7 part 2 answer: ", getWire(fname, a))