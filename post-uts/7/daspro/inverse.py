def invers(list1):
	if len(list1)==0:
		return list1
	else:
		return list1[-1:]+invers(list1[:-1])

print(invers([1,2,3,4]))