def isLast(x,list):
	if len(list) == 0:
		return False
	if len(list) == 1:
		if(list[0] == x):
			return True
		else:
			return False
	else:
		return isLast(x,list[1:])

print(isLast(1,[]))