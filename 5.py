def goes_through(line,point_x,point_y):
	line_x1,line_y1,line_x2,line_y2 = line
	if  abs(line_x1-point_x) == abs(line_y1-point_y) and abs(line_x2-point_x) == abs(line_y2-point_y) and abs(line_x1-line_x2) == abs(line_y1-line_y2):
		if point_x in range(line_x1,line_x2) or point_x in range(line_x1,line_x2,-1) or point_x == line_x2 or point_x == line_x1:
					
			return True
	if (line_x1 == point_x and line_x2 == point_x and (point_y in range(line_y1,line_y2+1) or point_y in range(line_y2,line_y1+1))) or (line_y1 == point_y and line_y2 == point_y and (point_x in range(line_x1,line_x2+1) or point_x in range(line_x2,line_x1+1))):
			
		return True
	return False
points = 0
infile = open("5.txt")
lines = [l.strip("\n").split(' -> ') for l in infile]
lines2 = [[int(line[0].split(',')[0]),int(line[0].split(',')[1]),int(line[1].split(',')[0]),int(line[1].split(',')[1])] for line in lines]
lines = lines2
for x in range(1000):
	print(x)
	for y in range(1000):
		if sum([goes_through(line,x,y) for line in lines])>1:
			points+=1
print(points)