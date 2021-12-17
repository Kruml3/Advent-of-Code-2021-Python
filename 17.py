import re
lines = list(map(int, re.findall(r'\d+', open("17.txt").readline())))
multiples = [1,1,-1,-1]
ints = [i*j for i,j in zip(lines,multiples)] 
xmin,xmax,ymin,ymax = ints

yVmax = int(ymin*(ymin+1)/2)
print(yVmax)
score = 0
for i in range(ymin-1,-ymin+1):
	for j in range(xmax+1):
		ci = i
		cj = j
		x,y = (0,0)
		while x<xmax and y>ymin:
			x += cj
			y += ci
			if cj > 0:
				cj -= 1
			ci -= 1
			if x <= xmax and x >= xmin and y <=ymax and y >= ymin:
				score += 1
				break
print(score)