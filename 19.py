import itertools
lines = [l.strip('\n') for l in open("19.txt")]
scanners = []
sc = []
for l in lines:
	if not l:
		scanners.append(sc)
	elif l[1] == '-':
		sc = []
	else:
		sc.append([int(x) for x in l.split(',')])
scanners.append(sc)
scLen = len(scanners)

def match(tr1,tr2,swaps):
	swaps = swaps % 2
	if swaps == 0:
		for x in [(1,1,1),(-1,1,-1),(1,-1,-1),(-1,-1,1)]:
			tr21 = [m*n for m,n in zip(tr2,x)] 
			if tr1 == tr21:
				return True, tr1, tr2, x
	if swaps == 1:
		for x in [(-1,1,1),(1,-1,1),(1,1,-1),(-1,-1,-1)]: 
			tr22 = [m*n for m,n in zip(tr2,x)] 
			if tr1 == tr22:
				return True, tr1, tr2, x
	return False, tr1, tr2, x

def matchTriplet(tr1,tr2):
	for x,y,z in itertools.permutations(range(3),3):
		swaps = 0
		if x>y:
			swaps += 1
		if x>z: 
			swaps += 1
		if y>z:
			swaps += 1
		mat, t1, t2, mul = match(tr1,[tr2[x],tr2[y],tr2[z]],swaps)
		if mat:
			return True, tr1, tr2, (x,y,z), mul
	return False, tr1, tr2, (0,0,0), (1,1,1)

def rel(scan,index):
	return [[x-scan[index][0],y-scan[index][1],z-scan[index][2]] for x,y,z in scan[:index]+scan[index+1:]]

def antirel(absol,rel,index):
	r1 = [[absol[i]+r[i] for i in range(3)] for r in rel[:index]]
	r2 = [[absol[i] for i in range(3)]] 
	r3 = [[absol[i]+r[i] for i in range(3)] for r in rel[index:]]
	return r1+r2+r3

def transformCoor(coor,x,y,z,mul):
	return [a*b for a,b in zip([coor[x],coor[y],coor[z]],mul)]


def matchScans(scan1,scan2):
	for i,j in enumerate(scan1):
		for k,l in enumerate(scan2[:-12]):
			score = 0
			s1 = rel(scan1,i)
			s2 = rel(scan2,k)
			for trip1 in s1:
				for trip2 in s2:
					possible = True
					for k in range(3):
						if abs(trip1[k]) not in [abs(trip2[l]) for l in range(3)]:
							possible = False
					if possible:
						mat, tr1, tr2, (x,y,z), mul = matchTriplet(trip1,trip2)
						if mat:
							score += 1
						if score == 11:
							s2 = [transformCoor(trip,x,y,z,mul) for trip in s2]
							s2 = antirel(j,s2,k)
							return s2, k, transformCoor(l,x,y,z,mul)
	return [], 0,[0,0,0]

def manhattan(a,b,c,x,y,z):
	return abs(a-x)+abs(b-y)+abs(c-z)

banned = [0]
scanPos = []
while len(banned) < scLen:
	# print("banned: " + str(banned))
	for i,scan in enumerate(scanners):
		if i in banned: 
			continue
		s2, k, relCoor = matchScans(scanners[0],scanners[i])
		if s2:
			scanners[0] = list(set.union(set(map(tuple, scanners[0])),set(map(tuple, s2))))
			scanPos.append([s2[k][p] - relCoor[p] for p in range(3)])
			banned.append(i)
print(len(scanners[0]))
manh = []
for i,j in itertools.permutations(scanPos,2):
	manh.append(manhattan(*i,*j))
print(max(manh))