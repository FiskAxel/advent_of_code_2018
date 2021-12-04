def main():
	with open('input19.txt', 'r') as puzzleInput:
		ipReg = int(puzzleInput.readline()[4])
		input = puzzleInput.readlines()
		codes = [i.strip() for i in input]
		reg = [0, 0, 0, 0, 0, 0]
		#print(f"Part 1: {bruteForce(reg, ipReg, codes)}")
		print(f"Part 1: {translation(False)}")
		print(f"Part 2: {translation(True)}")

def translation(part2):
	a, b, c, d, e = 0, 0, 0, 1, 0
	c += 2
	c *= c
	c *= 19 #ip
	c *= 11
	e += 1
	e *= 22 #ip
	e += 19
	c += e
	if part2:
		e = 27 #ip
		e *= 28 #ip
		e += 29 #ip
		e *= 30 #ip
		e *= 14
		e *= 32 #ip
		c += e
	while d <= c:
		if c % d == 0:
			a += d
		d += 1
	return a

# Runs in less than 2 minutes for part 1 :)
def bruteForce(reg, ipReg, codes):
	ip = 0
	while ip < len(codes):
		s = codes[ip].rsplit()
		ins = s[0]
		c = [int(s[i]) for i in range(1, 4)]
		reg[ipReg] = ip
		if ins == "addr":
			addr(reg, c[0], c[1], c[2])
		elif ins == "addi":
			addi(reg, c[0], c[1], c[2])
		elif ins == "mulr":
			mulr(reg, c[0], c[1], c[2])
		elif ins == "muli":
			muli(reg, c[0], c[1], c[2])
		elif ins == "banr":
			banr(reg, c[0], c[1], c[2])
		elif ins == "bani":
			bani(reg, c[0], c[1], c[2])
		elif ins == "borr":
			borr(reg, c[0], c[1], c[2])
		elif ins == "bori":
			bori(reg, c[0], c[1], c[2])
		elif ins == "setr":
			setr(reg, c[0], c[1], c[2])
		elif ins == "seti":
			seti(reg, c[0], c[1], c[2])
		elif ins == "gtir":
			gtir(reg, c[0], c[1], c[2])
		elif ins == "gtri":
			gtri(reg, c[0], c[1], c[2])
		elif ins == "gtrr":
			gtrr(reg, c[0], c[1], c[2])
		elif ins == "eqir":
			eqir(reg, c[0], c[1], c[2])
		elif ins == "eqri":
			eqri(reg, c[0], c[1], c[2])
		elif ins == "eqrr":
			eqrr(reg, c[0], c[1], c[2])
		ip = reg[ipReg]
		ip += 1
	return reg[0]
def addr(reg, a, b, c):
	reg[c] = reg[a] + reg[b]
def addi(reg, a, b, c):
	reg[c] = reg[a] + b
def mulr(reg, a, b, c):
	reg[c] = reg[a] * reg[b]
def muli(reg, a, b, c):
	reg[c] = reg[a] * b
def banr(reg, a, b, c):
	reg[c] = reg[a] & reg[b]
def bani(reg, a, b, c):
	reg[c] = reg[a] & b
def borr(reg, a, b, c):
	reg[c] = reg[a] | reg[b]
def bori(reg, a, b, c):
	reg[c] = reg[a] | b
def setr(reg, a, b, c):
	reg[c] = reg[a]
def seti(reg, a, b, c):
	reg[c] = a
def gtir(reg, a, b, c):
	if a > reg[b]:
		reg[c] = 1
	else:
		reg[c] = 0
def gtri(reg, a, b, c):
	if reg[a] > b:
		reg[c] = 1
	else:
		reg[c] = 0
def gtrr(reg, a, b, c):
	if reg[a] > reg[b]:
		reg[c] = 1
	else:
		reg[c] = 0
def eqir(reg, a, b, c):
	if a == reg[b]:
		reg[c] = 1
	else:
		reg[c] = 0
def eqri(reg, a, b, c):
	if reg[a] == b:
		reg[c] = 1
	else:
		reg[c] = 0
def eqrr(reg, a, b, c):
	if reg[a] == reg[b]:
		reg[c] = 1
	else:
		reg[c] = 0

main()