import re
import math

def main():
    with open('input24.txt', 'r') as puzzleInput:
        input = puzzleInput.read()
        armyInstructions = input.split('\n\n')
        
    print(f'Part 1: {battle(armyInstructions, 0) * -1}')
    result, boost = 0, 0
    while result <= 0:
        boost += 1
        result = battle(armyInstructions, boost)
        print(f'Result: {result} Boost: {boost}')
    print(f'Part 2: {result}')

# returns numbers of surviving units as negativ if infection wins
def battle(armyInstructions, boost):
    immuneSystem = createArmy(armyInstructions[0], boost)
    infection = createArmy(armyInstructions[1], 0)

    while True:
        immuneSystem.sort(key=lambda x : x.initiative, reverse=True)
        immuneSystem.sort(key=lambda x : x.effectivePower(), reverse=True)
        infection.sort(key=lambda x : x.initiative, reverse=True)
        infection.sort(key=lambda x : x.effectivePower(), reverse=True)
        targetSelection(immuneSystem, infection)
        targetSelection(infection, immuneSystem)
        attacking(immuneSystem, infection)
        funerals(immuneSystem)
        funerals(infection)
        if len(immuneSystem) == 0 or len(infection) == 0:
            break
        if tie(immuneSystem, infection):
            return 0
    return totalUnits(immuneSystem) - totalUnits(infection) 

def targetSelection(attackers, defenders):
    chosenTargets = []
    for group in attackers:
        group.setTarget(None)
        evaluation = []
        for defender in defenders:
            if defender in chosenTargets:
                continue
            dmg = damageMultiplier(group.type, defender.immuneTo, defender.weakTo)
            if dmg != 0:
                evaluation.append([dmg, defender.effectivePower(), defender.initiative, defender])

        if len(evaluation) > 0:
            evaluation.sort(reverse=True)
            d = evaluation[0][3] # chosen target object
            group.setTarget(d)
            chosenTargets.append(d) 

def attacking(imm, inf):
    groups = imm + inf
    groups.sort(key=lambda x : x.initiative, reverse=True)
    for group in groups:
        if group.target == None or group.units <= 0:
            continue
        target = group.target
        dmg = damageMultiplier(group.type, target.immuneTo, target.weakTo)
        kills = math.floor((dmg * group.effectivePower()) / target.hp)
        target.getUnitsKilled(kills)

def funerals(army):
    for group in army[:]:
        if group.units <= 0:
            army.remove(group)

def tie(imm, inf):
    if len(imm) == 1 and len(inf) == 1:
        if imm[0].cantKill(inf[0]) and inf[0].cantKill(imm[0]):
            return True
    return False

def totalUnits(army):
    sum = 0
    for group in army:
        sum += group.units
    return sum

def damageMultiplier(atkType, immuneTo, weakTo):
    if atkType in immuneTo:
        return 0
    if atkType in weakTo:
        return 2
    return 1

def createArmy(recipe, boost):
    army = []
    s = recipe.split('\n')
    armyName = s.pop(0)[:-1]
    for group in s:
        nums = [int(x) for x in re.findall('\d+', group)]
        units, hp, damage, initiative = nums[0], nums[1], nums[2], nums[3]
        type = re.findall(f'does {damage} (\w+) ', group)[0]
        weakTo = re.findall('weak to ([\w,\s]+)', group)
        immuneTo = re.findall('immune to ([\w,\s]+)', group)
        if len(weakTo) > 0:
            weakTo = weakTo[0].split(', ')
        if len(immuneTo) > 0:
            immuneTo = immuneTo[0].split(', ')
        army.append(ArmyGroup(units, hp, damage + boost, type, weakTo, immuneTo, initiative, armyName))
    return army

class ArmyGroup:
    def __init__(self, u, h, d, t, w, im, i, n):
        self.units = u
        self.hp = h
        self.damage = d
        self.type = t
        self.weakTo = w
        self.immuneTo = im
        self.initiative = i
        self.armyName = n
        self.target = None

    def setTarget(self, target):
        self.target = target
    def effectivePower(self):
        return self.units * self.damage
    
    def getUnitsKilled(self, num):
        self.units -= num
    
    def cantKill(self, target):
        if self.effectivePower() < target.hp:
            return True
        if self.type in target.immuneTo:
            return True
        return False


main()