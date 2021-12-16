from copy import deepcopy
lines = [[int(char) for char in l.strip('\n')] for l in open("15.txt")]
paths = [[99999 for k in range(len(lines[0]))] for i in range(len(lines))]
paths[0][0]=0
for k in range(len(lines[0])):
	paths[0][k] = sum([lines[0][y] for y in range(1,k+1)])
def iter(lines,paths):
	change = True
	while change:
		change = False
		for i,j in enumerate(paths):
			for k,l in enumerate(j):
				if i>0 and paths[i][k] > paths[i-1][k]+lines[i][k]:
					paths[i][k] = paths[i-1][k]+lines[i][k]
					change = True
				if i<len(lines)-1 and paths[i][k] > paths[i+1][k]+lines[i][k]:
					paths[i][k] = paths[i+1][k]+lines[i][k]
					change = True
				if k>0 and paths[i][k] > paths[i][k-1]+lines[i][k]:
					paths[i][k] = paths[i][k-1]+lines[i][k]
					change = True
				if k<len(lines[0])-1 and paths[i][k] > paths[i][k+1]+lines[i][k]:
					paths[i][k] = paths[i][k+1]+lines[i][k]
					change = True
	return (paths[len(lines)-1][len(lines[0])-1])
print(iter(lines,paths))
x = len(lines[0])
y = len(lines)

for k,l in enumerate(lines):
	newLine = []
	for r in range(5):
		lineCopy = deepcopy(lines[k])
		newLine.extend(lineCopy)
	lines[k] = newLine
	for i in range(5*x): lines[k][i] += i//x
newLines = []
for r in range(5):
	linesCopy = deepcopy(lines)
	newLines.extend(linesCopy)
lines = newLines
for i in range(5*y):
	for j in range(5*x):
		lines[i][j] += i//y
		lines[i][j] = lines[i][j]//10+lines[i][j]%10
paths = [[99999 for k in range(len(lines[0]))] for i in range(len(lines))]
paths[0][0]=0
print(iter(lines,paths))