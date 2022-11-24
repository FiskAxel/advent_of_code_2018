from z3 import *

def main():
    with open('input23.txt', 'r') as puzzleInput:
        input = puzzleInput.readlines()
        nanobots = []
        for i in input:
            s = i.split('>, r=')
            nanobots.append(Nanobot(
                int(s[1].strip()), 
                [int(x) for x in s[0][5:].split(',')]
            )) 
        nanobots.sort(key=lambda x: x.radius, reverse=True)

    botStatus = 0
    for bot in nanobots:
        distance = manhattanDistance3D(nanobots[0].position, bot.position)
        if (distance <= nanobots[0].radius):
            botStatus += 1
    print(f"Part 1: {botStatus}")

    # For part 2 my Bron Kerbosch implementation was way to slow so I went to  
    # the reddit thread and then tried out z3. 

    opt = Optimize()
    x, y, z = Int('x'), Int('y'), Int('z')
    distanceToOrigo = Int('distanceToOrigo')
    opt.add(distanceToOrigo == zabs(x) + zabs(y) + zabs(z))

    botStatus = []
    for i, bot in enumerate(nanobots):
        bx, by, bz = bot.position[0], bot.position[1], bot.position[2]
        inRange = Int(f'inRange{i}')
        opt.add(inRange ==
            If(zabs(x - bx) + zabs(y - by) + zabs(z - bz) <= bot.radius, 1, 0)    
        )
        botStatus.append(inRange)
    botsInRange = Int('botsInRange')
    opt.add(botsInRange == Sum(botStatus))

    opt.maximize(botsInRange)
    opt.minimize(distanceToOrigo)
    opt.check()
    model = opt.model()
    print(f"Part 2: {model[distanceToOrigo]}")


def zabs(num):
    return If(num > 0, num, -num)

def manhattanDistance3D(pos1, pos2):
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return abs(x2-x1) + abs(y2-y1) + abs(z2-z1)

class Nanobot:
    def __init__(self, r, p):
        self.radius = r
        self.position = p






# too slow...
def bronKerbosch(r, p, x):
    global biggestClique
    if len(p) == 0 and len(x) == 0:
        if len(biggestClique) < len(r):
            biggestClique = r
    for bot in p[:]:
        newR = r.copy()
        newR.append(bot)
        bronKerbosch(newR, botNeighbours(bot, p), botNeighbours(bot, x))
        p.remove(bot)
        x.append(bot)        
def botNeighbours(bot, bots):
    neighbours = []
    for b in bots:
        if b == bot:
            continue
        if botsAreWithinRange(bot, b):
            neighbours.append(b)
    return neighbours
def botsAreWithinRange(bot1, bot2):
    d = manhattanDistance3D(bot1.position, bot2.position)
    if d <= bot1.radius and d <= bot2.radius:
        return True
    return False
def botIsWithinRange(bot, point):
    if manhattanDistance3D(bot.position, point) <= bot.radius:
        return True
    return False

main()