def ismember(x,list):
	if len(list) == 0:
		return False
	if list[0] == x:
		return True
	else:
		return ismember(x,list[1:])

print(ismember(2,[1,4,3,2]))