from copy import deepcopy
file = open("20.txt")
N = 51
algo = file.readline()
file.readline()
lines = [l.strip('\n') for l in file]
newLines = []
pad = '.'*N
for l in lines:
	l = pad+l[:]+pad
	newLines.append(l)
lines = newLines
emptyLine = ''
fullLine = ''
for i in range(len(lines[0])):
	emptyLine += '.'
	fullLine += '#'
padlines = [emptyLine for i in range(N)]
lines = [*padlines,*lines,*padlines]
for n in range(N-1):
	lineCopy = deepcopy(lines)
	if n%2 == 0:
		lineCopy = [fullLine for i in range(len(lineCopy))]
	if n%2 == 1:
		lineCopy = [emptyLine for i in range(len(lineCopy))]
	for k,l in enumerate(lines):
		for i,c in enumerate(l):
			if k > N-2-n and k < len(lines)-N+n+1 and i > N-2-n and i < len(lines[0]) - N+n+1:
				strV = ""
				neighbors = [(lines[i+a][k+b]) for a,b in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]]
				for v in neighbors:
					if v == '#':
						strV += '1'
					else:
						strV += '0'
				v = int(strV,2)
				lineCopy[i] = lineCopy[i][:k]+algo[v]+lineCopy[i][k+1:]
	lines = deepcopy(lineCopy)
	if n in [1,49]:
		score = 0
		for l in lines:	
			for c in l:
				if c == '#':
					score += 1
		print(score)
