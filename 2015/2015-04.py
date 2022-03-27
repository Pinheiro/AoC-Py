import hashlib

def Stuffer(secretKey, nZeros):
    r = 0
    s = "0" * nZeros
    while True:
        r = r + 1
        k = secretKey + str(r)
        h = hashlib.md5(k.encode())
        if h.hexdigest()[0:nZeros]==s:
            break
    return r

assert Stuffer("abcdef", 5) == 609043
assert Stuffer("pqrstuv", 5) == 1048970

print()
print("event 2015 day 4 part 1 answer: ", Stuffer("iwrupvqb", 5))

print()
print("event 2015 day 4 part 2 answer: ", Stuffer("iwrupvqb", 6))