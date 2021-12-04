def main():
	with open('input05.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()
		p = []
		for c in input[0]:
			p.append(c)
		b = p.copy()
		fullyReact(b)
		result = len(b)
		print(f"Part 1: {result}")

		min = result
		for i in range(65, 91):
			b = p.copy()
			removeCc(b, i)
			fullyReact(b)
			if len(b) < min:
				min = len(b)
		print(f"Part 2: {min}") # Runs in about 10 seconds

def fullyReact(p):
	i = 0
	while i < len(p) - 1:
		if abs(ord(p[i]) - ord(p[i + 1])) == 32:
			p.pop(i)
			p.pop(i)
			i -= 2
		i += 1
def removeCc(p, num):
	i = 0
	while i < len(p):
		n = ord(p[i])
		if n == num or n == num + 32:
			p.pop(i)
			continue
		i += 1

main()