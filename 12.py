lines = [l.strip('\n').split('-') for l in open("12.txt")]
connections = {}
for l in lines:
	connections[l[0]] = connections.get(l[0],[])
	connections[l[1]] = connections.get(l[1],[])
	connections[l[0]].append(l[1])
	connections[l[1]].append(l[0])

def findRts(start,lowerVisited,twiceVisited,part):
	if start == 'end':
		return 1
	rtsNumber = 0
	for choice in connections[start]:
		if choice.islower():
			if choice not in lowerVisited:
				rtsNumber += findRts(choice,lowerVisited+[choice],twiceVisited,part)
			else: 
				if part == 1:
					continue
				if twiceVisited or choice == 'start' or choice == 'end':
					continue
				else:
					rtsNumber += findRts(choice,lowerVisited+[choice],[choice],part)
		else:
			rtsNumber += findRts(choice,lowerVisited,twiceVisited,part)
	return rtsNumber
print(findRts("start",["start"],[],1))
print(findRts("start",["start"],[],2))