# Ugly and slow but it works...
def main():
	with open('input25.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()
		points = []
		for i in input:
			points.append([int(j.strip()) for j in i.split(',')])	
		constellations = []
		matchPoints(points, constellations)
		matchListsOfPoints(constellations)
		result = len(constellations)
		print(f"Part 1: {result}")

def matchPoints(points, constellations):
	if len(points) == 0:
		return
	constellation = [points[0]]
	for i in range(1, len(points)):
		if manhattan(points[0], points[i]) <= 3:
			constellation.append(points[i])
	constellations.append(constellation)
	for i in constellation:
		points.remove(i)
	matchPoints(points, constellations)
def matchListsOfPoints(constellations):
	prevLen = len(constellations)
	while (True):
		for i in range(len(constellations)):
			j = i + 1
			while j < len(constellations):
				if sameConstellation(i, j, constellations):
					merge(i, j, constellations)
					continue
				j += 1
		if prevLen == len(constellations):
			return

def manhattan(p1, p2):
	sum = 0
	for a, b in zip(p1, p2):
		sum += abs(a - b)
	return sum
def sameConstellation(i, j, constellations):
	for p1 in constellations[i]:
		for p2 in constellations[j]:
			if manhattan(p1, p2) <= 3:
				return True
	return False
def merge(i, j, constellations):
	for c in constellations[j]:
		constellations[i].append(c)
	constellations.pop(j)

main()