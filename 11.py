lines = [[int(char) for char in l.strip('\n')] for l in open("11.txt")]
flashScore = 0
def cyklus(lines):
	score = 0
	flashNew = []
	flash = []
	for i,j in enumerate(lines):
		for k,l in enumerate(j):
			lines[i][k] += 1
			if lines[i][k]>9:
				flashNew.append([i,k])
				flash.append([i,k])
	while flashNew:
		for [i,k] in flashNew:
			if i > 0:
				lines[i-1][k] += 1
				if k > 0:
					lines[i-1][k-1] += 1
				if k < len(lines[0])-1:
					lines[i-1][k+1] += 1
			if i < len(lines)-1:
				lines[i+1][k] += 1
				if k > 0:
					lines[i+1][k-1] += 1
				if k < len(lines[0])-1:
					lines[i+1][k+1] += 1
			if k > 0:
				lines[i][k-1] += 1
			if k < len(lines[0])-1:
				lines[i][k+1] += 1
		flashNew = []
		for i,j in enumerate(lines):
			for k,l in enumerate(j):
				if lines[i][k]>9 and [i,k] not in flash:
					flashNew.append([i,k])
					flash.append([i,k])
	for i,j in enumerate(lines):
		for k,l in enumerate(j):
			if [i,k] in flash:
				lines[i][k] = 0
				score += 1
	if len(flash) == len(lines)*len(lines[0]):
		return -1
	return score
simul = False
run = 0
while not simul:
	run += 1
	s = cyklus(lines)
	if s>=0:
		flashScore += s
	else: simul = True
print(flashScore)
print(run)
