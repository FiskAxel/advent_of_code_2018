input = "513401"
elf1 = 0
elf2 = 1
r = '37'
while input not in r[-7:]:
#while len(r) < int(input) + 10:
	r += str(int(r[elf1]) + int(r[elf2]))
	elf1 = (elf1 + 1 + int(r[elf1])) % len(r)
	elf2 = (elf2 + 1 + int(r[elf2])) % len(r)
print(f"Part 1: {r[int(input):int(input) + 10]}") # Takes a couple of seconds
print(f"Part 2: {len(r) - len(input)}") # Runs in about 3 minutes