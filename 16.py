line = open("16.txt").readline()
score = 0

def operate(type_ID, new, old):
	if type_ID == 0:
		return new+old
	if type_ID == 1:
		return new*old
	if type_ID == 2:
		return min(new,old)
	if type_ID == 3:
		return max(new,old)
	if type_ID == 5:
		if new < old:
			return 1
		else:
			return 0
	if type_ID == 6:
		if new > old:
			return 1
		else:
			return 0
	if type_ID == 7:
		if new == old:
			return 1
		else:
			return 0

def decode(bin_str,index_0,verbose, depth):
	value = -1
	index = index_0
	score = int(bin_str[index:index+3],2)
	type_ID = int(bin_str[index+3:index+6],2)
	if verbose:
		print(bin_str[index_0:index_0+22], index_0, score, type_ID, depth)
	if type_ID == 4:
		literal = ''
		index += 6
		next_group = True
		while next_group:
			if bin_str[index] == '0':
				next_group = False
			literal += bin_str[index+1:index+5]
			index += 5
		literal = int(literal,2)
		if verbose:
			print("LITERAL: " + str(literal))
		value = literal
	else:
		index += 7
		if bin_str[index-1] == '0':
			length = int(bin_str[index:index+15],2)
			if verbose:
				print("PACKET_LENGTH: " + str(length))
			index += 15
			package = 0
			while package<length:
				i, s, v = decode(bin_str,index, verbose, depth+1)
				package += i 
				index += i
				if verbose:
					print("PACKAGE_CURR: " + str(package))
				score += s
				if value == -1:
					value = v
				else:
					value = operate(type_ID, v, value)
		else:
			packet_num = int(bin_str[index:index+11],2)
			if verbose:
				print("PACKET_NUM: " + str(packet_num))
			index += 11
			for i in range(packet_num):
				i, s, v = decode(bin_str, index, verbose, depth+1)
				index += i
				score += s
				if value == -1:
					value = v
				else:
					value = operate(type_ID, v, value)
	if verbose:
		print(index, index_0, index - index_0)
	return index - index_0, score, value

bin_str = bin(int(line, 16))[2:].zfill(len(line)*4)
i, s, v = decode(bin_str,0,0,0)
print(s)
print(v)