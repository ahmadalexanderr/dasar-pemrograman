def elementN(x,list1):
	if len(list1) == 0:
		return 0
	if list1[0] == x:
		return 0
	else:
		return 1+elementN(x,list1[1:])

list1 = [3,2,4,2,1]

print(elementN(1,list1))

if elementN(1,list1) == len(list1):
	print("tidak ketemu")
else:
	print("ketemu")