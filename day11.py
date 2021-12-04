import numpy as np
def main():
	input = 7347
	grid = np.zeros((300, 300))
	powerLvls(grid, input)
	result = powerfull3x3SquareXY(grid)
	print(f"Part 1: {result}") # Takes a couple of seconds
	result = powerfullestSquareXY(grid)
	print(f"Part 2: {result}") # Takes about 10 seconds

def powerLvls(grid, serialNum):
	for y in range(300):
		for x in range(300):
			rackID = (x + 1) + 10
			powerLvl = rackID * (y + 1)
			powerLvl += serialNum
			powerLvl *= rackID
			powerLvl = int(str(powerLvl)[-3:-2])
			powerLvl -= 5
			grid[y][x] = powerLvl
def powerfull3x3SquareXY(grid):
	max = 0
	coord = [0, 0]
	for y in range(300 - 2):
		for x in range(300 - 2):
			square = grid[y:y+3, x:x+3]
			sum = square.sum()
			if sum > max:
				max = sum
				coord = [x + 1, y + 1]
	return str(f"{coord[0]},{coord[1]}")
def powerfullestSquareXY(grid):
	max = 0
	mSize = 3
	coord = [0, 0]
	for size in range(4, 16):
		for y in range(300 - (size - 1)):
			for x in range(300 - (size - 1)):
				square = grid[y:y+size, x:x+size]
				sum = square.sum()
				if sum > max:
					max = sum
					mSize = size
					coord = [x + 1, y + 1]
	return str(f"{coord[0]},{coord[1]},{mSize}")

main()