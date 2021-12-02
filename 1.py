infile = open('1.txt')
y = []
x = 100000
x2 = 100000
x3 = 100000
z = 0
z2 = 0
for line in infile:
	if int(line)+x+x2 > x+x2+x3:
		z2 += 1
	if int(line) > x:
		z += 1
	x3 = x2
	x2 = x
	x = int(line)
print(z)
print(z2)