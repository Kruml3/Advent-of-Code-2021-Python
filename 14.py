from collections import Counter
file = open("14.txt")
start = file.readlines(1)[0].strip("\n")
file.readline()
lines = [l.strip('\n').split(' -> ') for l in file]
lines = dict(lines)
copyStart = start
for i in range(10):
	pairs = [start[a]+start[b] for a,b in zip(range(len(start)-1),range(1,len(start)))]
	string = ""
	for p in pairs:	
		string += p[0] + lines.get(p,'')
	string += pairs[-1][1]
	start = string
c = Counter(start)
print(max(c.values())-min(c.values()))

pairs = [copyStart[a]+copyStart[b] for a,b in zip(range(len(copyStart)-1),range(1,len(copyStart)))]
pairCount = {}
for p in pairs:
	pairCount[p] = pairCount.get(p,0) + 1
for i in range(40):
	newDict = {}
	for k,v in zip(pairCount.keys(),pairCount.values()):
		k1 = k[0]+lines[k]
		k2 = lines[k]+k[1]
		newDict[k1] = newDict.get(k1,0) + v
		newDict[k2] = newDict.get(k2,0) + v
	pairCount = newDict
singleCount = {}
for k,l in pairCount:
	v = pairCount[k+l]
	singleCount[k] = singleCount.get(k,0)+v
singleCount[start[-1]]+=1

print(max(singleCount.values())-min(singleCount.values()))