from collections import deque
def main():
	players = 435
	last = 71184
	print(f"Part 1: {play(players, last)}")
	print(f"Part 2: {play(players, last * 100)}")

def play(p, l):
	scores = {}
	for i in range(p):
		scores[i] = 0
	circle = deque([0])
	for i in range(l):
		if (i + 1) % 23 == 0:
			circle.rotate(7)
			scores[i % p] += (i + 1) + circle.pop()
			circle.rotate(-1)
		else:
			circle.rotate(-1)
			circle.append(i + 1)
	return max(scores.values())

main()