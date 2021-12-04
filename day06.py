import numpy as np
def main():
	with open('input06.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()
		xc = [int(i[:i.index(",")]) for i in input]
		yc = [int(i[i.index(" ") + 1:].rstrip()) for i in input]
		field = np.empty((max(yc) + 1, max(xc) + 1))
		for y in range(len(field)):
			for x in range(len(field[y])):
				field[y][x] = closest(x, y, xc, yc)
		infs = np.concatenate([field[0,:], field[-1,:], field[:,0], field[:,-1]])
		infs = set(infs)
		result = 0
		for i in range(1, len(input) + 1):
			if i not in infs:
				count = len(field[field == i])
				if count > result:
					result = count
		print(f"Part 1: {result}") # runs in about 10 seconds

		result = 0
		for y in range(len(field)):
			for x in range(len(field[y])):
				if inRegion(x, y, xc, yc):
					result += 1
		print(f"Part 2: {result}") # runs in another 10 seconds

def closest(x, y, xc, yc):
	min = 10000
	for i in range(len(xc)):
		dist = abs(y - yc[i]) + abs(x - xc[i])
		if dist < min:
			min = dist
			output = i + 1
		elif dist == min:
			output = 0
	return int(output)
def inRegion(x, y, xc, yc):
	dist = 0
	for i in range(len(xc)):
		dist += abs(y - yc[i]) + abs(x - xc[i])	
	if dist >= 10000:
		return False
	return True

main()