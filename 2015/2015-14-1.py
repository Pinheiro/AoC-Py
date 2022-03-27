import re

def distance(reindeer, time):
    speed = int(reindeer[1])
    flyTime = int(reindeer[2])
    restTime = int(reindeer[3])
    cycleTime = flyTime + restTime
    cycles = time // cycleTime
    remindTime = time % cycleTime
    return (cycles * flyTime + min(remindTime, flyTime)) * speed

def solve(fname, time):
    pattern = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')
    stats = pattern.findall(open(fname).read())
    stats = [list(s) for s in stats]
    dists = [distance(s, time) for s in stats]
    return max(dists)
    
assert solve('2015-14-0.txt', 1000) == 1120
print()
print("event 2015 day 14 part 1 answer: ", solve('2015-14.txt', 2503))