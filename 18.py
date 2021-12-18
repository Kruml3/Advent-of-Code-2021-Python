lines = [l.strip("\n") for l in open("18.txt")]
result = ""

def leftmost(arr):
	while len(arr) > 1:
		arr = arr[0]
	return arr

def rightmost(arr):
	while len(arr) > 1:
		arr = arr[1]
	return arr

def transform1(snailList,depth,toleft,toright):
	change = False
	if len(snailList) == 2:
		if depth > 3:
			if toleft:
				toleft[0] += snailList[0][0]
			if toright:
				toright[0] += snailList[1][0]
			return ([0], True)

		snailList[0], change = transform1(snailList[0],depth+1,toleft,leftmost(snailList[1]))
		if change: 
			return snailList, True
		snailList[1], change = transform1(snailList[1],depth+1,rightmost(snailList[0]),toright)
		if change:
			return snailList, True
	return snailList, change

def transform2(snailList,depth):
	change = False
	if len(snailList) == 2:
		snailList[0], c1 = transform2(snailList[0],depth+1)
		if c1: 
			return snailList, True
		snailList[1], c2 = transform2(snailList[1],depth+1)
		if c2: 
			return snailList, True
	if len(snailList) == 1:
		if snailList[0] > 9:
			change = True
			snailList = [[snailList[0]//2],[snailList[0]-snailList[0]//2]] 
	return snailList, change


def magn(snailNum):
	if len(snailNum) == 2:
		return 3*magn(snailNum[0])+2*magn(snailNum[1])
	return snailNum[0]

def conv(array):
	if type(array) == type([]):
		array[0] = conv(array[0])
		array[1] = conv(array[1])
		return array
	return [array]

def evalList(lines):
	result = conv(eval(lines[0]))
	for l in lines[1:]:
		l = conv(eval(l))
		result = [result, l]
		change = True
		while change:
			result, c1 = transform1(result,0,[],[])
			if not c1:
				result, c2 = transform2(result,0)
				if c2:
					c1 = True
			change = c1 or c2
	return result

print(magn(evalList(lines)))

tries = []
for i in range(len(lines)):
	for j in range(len(lines)):
		if i is not j:
			tries.append((i,j))
			
print(max([magn(evalList([lines[i],lines[j]])) for i,j in tries]))

