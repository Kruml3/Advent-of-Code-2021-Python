infile = open("3.txt")
lines = [l for l in infile]
ones = []
zeros = []
for i in range(len(lines[0])-1):
	one = (sum([int(x[i]) for x in lines]))
	ones.append(one)
	zeros.append(len(lines)-one)
binar = [1 if a>b else 0 for a,b in zip(ones,zeros)]
gamma = 0
for ele in binar:
    gamma = (gamma << 1) | ele
print(gamma*(gamma^(2**(len(lines[0])-1)-1)))
lines2 = lines.copy()
for i in range(len(lines[0])-1):
	one = (sum([int(x[i]) for x in lines]))
	one2 = (sum([int(x[i]) for x in lines2]))
	one_zero = "0"
	one_zero2 = "0"
	if one >= len(lines)/2:
		one_zero = "1"
	if one2 < len(lines2)/2:
		one_zero2 = "1"
	if(len(lines)>1):
		lines = [l for l in lines if l[i]==one_zero]
	if(len(lines2)>1):
		lines2 = [l for l in lines2 if l[i]==one_zero2]
print(int(lines[0],2)*int(lines2[0],2))

