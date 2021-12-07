infile = open("7.txt")
lines = [l.split(",") for l in infile]
numbers = [int(l) for l in lines[0]]
guess=0
sum1=1000000000
sum2=999999999
while(sum2<sum1):
	guess+=1
	sum1=sum2
	sum2=sum(list(map(lambda n: abs(n-guess), numbers)))
print(sum1)
guess=0
sum1=1000000000
sum2=999999999
while(sum2<sum1):
	guess+=1
	sum1=sum2
	sum2=sum(list(map(lambda n: (abs(n-guess)+1)*abs(n-guess)/2, numbers)))
print(sum1)