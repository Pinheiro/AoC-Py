import re

def str2bytes(string):
    return [ord(letter) for letter in string]

def increment(asc): # ascii codes (a-z) -> (97-122)
    return ((asc - 97) + 1) % 26 + 97

def replace(password, forbiddenletter, newletter):
    p = password.find(forbiddenletter)
    if p == -1:
        return password
    else:
        n = str2bytes(password)
        n[p] = ord(newletter)
        n[p+1:] = [ord('a')] * (len(n)-p-1)
        return ''.join(map(chr,n))

def nextpwd(pwd):
    newpwd = pwd
    i = -1
    while True:
        
        # increment password
        
        n = str2bytes(newpwd)
        n[i] = increment(n[i])
        while n[i]==97:
            i -= 1
            n[i] = increment(n[i])
        i = -1
        
        # requirement 1: increasing straight
        
        req1ok = any([n[i]+1==n[i+1] and n[i]+2==n[i+2] and n[i+1]+1==n[i+2] for i in range(len(newpwd)-2)])
        
        # requirement 2: forbidden letters
        
        newpwd = ''.join(map(chr,n))
        newpwd = replace(newpwd, 'i', 'j')
        newpwd = replace(newpwd, 'o', 'p')
        newpwd = replace(newpwd, 'l', 'm')
        req2ok = len(re.findall("[iol]", newpwd)) == 0
        
        # requirement 3: two pairs
        
        pattern = re.compile(r'(\w)\1.*(\w)\2')
        res = pattern.findall(newpwd)
        req3ok = len(res) > 0 and not all(element == res[0][0] for element in res[0])
        
        if req1ok and req2ok and req3ok:
            break
    
    return newpwd

assert nextpwd('abcdefgh') == 'abcdffaa'
assert nextpwd('ghijklmn') == 'ghjaabcc'

print()
r1 = nextpwd("vzbxkghb")
print("event 2015 day 11 part 1 answer: ", nextpwd("vzbxkghb"))

print()
print("event 2015 day 11 part 2 answer: ", nextpwd(r1))
