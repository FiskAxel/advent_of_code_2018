def main():
	with open('input02.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()
		twos = 0
		threes = 0
		for l in input:
			chars = {}
			for c in l:
				if c in chars:
					chars[c] += 1
				else:
					chars[c] = 1
			two = False
			three = False
			for c in chars:
				if chars[c] == 2:
					two = True
				elif chars[c] == 3:
					three = True
			if two:
				twos += 1
			if three:
				threes += 1

		result = twos * threes
		print(f"Part 1: {result}")

		# PART 2

		done = False
		for a in input:
			if done:
				break
			for b in input:
				if compare(a, b):
					result = getID(a, b)
					done = True
					break
		print(f"Part 2: {result}")

def compare(a, b):
	if a == b:
		return False
	dif = 0
	for c in range(len(a)):
		if a[c] != b[c]:
			dif += 1
		if dif > 1:
			return False
	return True
def getID(a, b):
	output = ""
	for c in range(len(a)):
		if a[c] == b[c]:
			output += a[c]
	return output

main()