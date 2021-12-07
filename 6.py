def production(lines):
	zeros = lines[0]
	for i in range(0,8):
		lines[i] = lines[i+1]
	lines[8] = zeros
	lines[6] += zeros
	return lines
infile = open("6.txt")
lines = [l.strip("\n").split(',') for l in infile]
lines = [int(l) for l in lines[0]]
lines = [lines.count(i) for i in range(9)]
for i in range(80):
	lines = production(lines)
print(sum(lines))
for i in range(80,256):
	lines = production(lines)
print(sum(lines))