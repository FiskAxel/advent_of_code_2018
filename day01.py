def main():
	with open('input01.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()
		result = 0
		for i in input:
			result += int(i)
		print(f"Part 1: {result}")
		# Runs in about 90 seconds
		print(f"Part 2: {part2(input)}")

def part2(input):
	prevs = []
	result = 0
	while True:
		for i in input:
			result += int(i)
			if result in prevs:	
				return result
			prevs.append(result)

main()