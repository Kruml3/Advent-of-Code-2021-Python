import math
infile = open("4.txt")
lines = [l for l in infile]
boards = {}
sums = {}
won = 0
boards_alive = list(range(100))
for i in range(2,len(lines)):
	boards[(i-2)//6] = boards.get((i-2)//6,[]) + [int(x) for x in lines[i].split()]
for board_num in range(len(boards)):
	sums[board_num] = [0,0,0,0,0,0,0,0,0,0]
for number in lines[0].split(','):
	number = int(number)
	for board_num in boards_alive:
		if number in boards[board_num]:
			index = boards[board_num].index(number)
			sums[board_num][index//5]+=1
			sums[board_num][index%5+5]+=1
			boards[board_num][boards[board_num].index(number)] = 0.0000001
	for board_num in boards_alive:
		if 5 in sums[board_num]:
			if won==99 or won==0:
				print(math.floor(sum(boards[board_num])*number))
			boards_alive.remove(board_num) 
			won+=1



