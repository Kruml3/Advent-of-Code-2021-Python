from collections import Counter
import math
lines = [l.strip("\n") for l in open("9.txt")]
result = 0
for i,j in enumerate(lines):
	for k,l in enumerate(j):
		adj = []
		if k>0:
			adj.append(j[k-1])
		if k<len(j)-1:
			adj.append(j[k+1])
		if i>0:
			adj.append(lines[i-1][k])
		if i<len(lines)-1:
			adj.append(lines[i+1][k])
		if l < min(adj):
			result+=int(l)+1
print(result)
lenx = len(lines[0])
leny = len(lines)
def basinSize(x,y,area):
	if x<0 or y<0 or x>=lenx or y>=leny:
		return 0
	if [x,y] in area:
		return 0
	if int(lines[x][y])==9:
		return 0
	area.append([x,y])
	value = basinSize(x-1,y,area)+basinSize(x+1,y,area)+basinSize(x,y+1,area)+basinSize(x,y-1,area)
	return 1+value
sizeList = [basinSize(x,y,[]) for x in range(lenx) for y in range(leny)]
sizeDict = dict(Counter(sizeList))
top3 = []
while len(top3)<3:
	m = max(sizeDict.keys())
	while m<=sizeDict[m]:
		if len(top3)<3:
			top3.append(m)
		sizeDict[m]-=m
	del sizeDict[m]
print(math.prod(top3))

