file = "8.txt"
lines =[[len(code) for code in l.split('|')[1].split()] for l in open(file)]
print(sum([sum([l.count(i) for i in [2,3,4,7]]) for l in lines]))
linesAns =[l.split('|')[1].split() for l in open(file)]
lines0=[l.split('|')[0].split() for l in open(file)]
lines1 =[[len(code) for code in l] for l in lines0]
def getNumbers(line):
	numDict = {42:0,17:1,34:2,39:3,30:4,37:5,41:6,25:7,49:8,45:9}
	chars = ['a','b','c','d','e','f','g']
	charDict = {}
	for char in chars:
		charDict[char] = sum([1 for l,i in zip(lines1[line],lines0[line]) if char in i])
	value = 0
	for i,j in enumerate(linesAns[line]):
		num = sum([charDict[char] for char in j])
		value+= numDict[num]*10**(len(linesAns[line])-i-1)
	return value
print(sum([getNumbers(l) for l in range(len(lines))])) 