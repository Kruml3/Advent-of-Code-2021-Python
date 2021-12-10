from statistics import median
lines = [l.strip("\n") for l in open("10.txt")]
openChars = ['(','[','{','<']
closeChars = [')',']','}','>']
values = {')':3,']':57,'}':1197,'>':25137}

def corrupted(line):
	chararray = []
	for char in line:
		if char in openChars:
			chararray.append(openChars.index(char))
		else:
			if chararray[-1]!=closeChars.index(char):
				return values[char]
			chararray.pop(-1)
	return 0

def completing(line):
	score = 0
	chararray = []
	for char in line:
		if char in openChars: 
			chararray.append(openChars.index(char))
		else:
			chararray.pop(-1)
	for char in chararray[::-1]:
		score *= 5
		score += char + 1
	return score

score = 0
newlines = []
for l in lines:
	sc = corrupted(l)
	if sc == 0:
		newlines.append(l)
	score += sc

print(score)
print(median([completing(l) for l in newlines]))