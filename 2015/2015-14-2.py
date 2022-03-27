import re

def distance(stat, time):
    speed = stat[1]
    flyTime = stat[2]
    restTime = stat[3]
    cycleTime = flyTime + restTime
    cycles = time // cycleTime
    remainingTime = time % cycleTime
    return (cycles * flyTime + min(remainingTime, flyTime)) * speed

def solve(fname, time):
    pattern = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')
    stats = pattern.findall(open(fname).read())
    stats = [list(s) for s in stats]
    for s in range(len(stats)):
        for i in range(3):
            stats[s][i + 1] = int(stats[s][i + 1])
    points = [0] * len(stats)
    for t in range(time):
        distances = [distance(s, t + 1) for s in stats]
        indices = [i for i, x in enumerate(distances) if x == max(distances)]
        for i in indices:
            points[i] += 1
    return max(points)
    
assert solve('2015-14-0.txt', 1000) == 689
print()
print("event 2015 day 14 part 2 answer: ", solve('2015-14.txt', 2503))