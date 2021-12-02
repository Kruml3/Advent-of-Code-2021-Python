infile = open('2.txt')
lines = [[x.split()[0],int(x.split()[1])] for x in infile.readlines()]
depth1 = 0
depth2 = 0
forward = 0
aim = 0
for l,d in lines:
	if l=="forward":
		forward+=d
		depth2+=d*aim
	if l=="backward":
		forward-=d
		depth2-=d*aim
	if l=="down":
		depth1+=d
		aim+=d
	if l=="up":
		depth1-=d
		aim-=d
print(forward*depth1)
print(forward*depth2)
