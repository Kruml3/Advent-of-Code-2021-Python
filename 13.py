file = "13.txt"
dots = [[int(num) for num in l.strip('\n').split(',')] for l in open(file) if len(l)>1 and len(l)<11]
folds = [[coor,int(val)] for coor,val in [l.split()[2].split('=') for l in open(file) if len(l)>10]]

def abso(num,val):
	return val - abs(num - val)
field1 = min([val for coor,val in folds if coor == 'x'])
field2 = min([val for coor,val in folds if coor == 'y'])

pr=True
for coor,val in folds:
	new_dots = []
	for x,y in dots:
		if coor == 'x':
			x = abso(x,val)
		else:
			y = abso(y,val)
		new_dots.append([x,y])
	dots = [list(x) for x in {(tuple(e)) for e in new_dots}]
	if pr:
		print(len(dots))
		pr=False
mapa = ['.'*field1]*field2
for i,j in enumerate(mapa):
	for k,l in enumerate(j):
		if [k,i] in dots:
			mapa[i]=mapa[i][:k] + '0' + mapa[i][k+1:]
for m in mapa:
	print(m)