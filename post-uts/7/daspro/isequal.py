def isEqual(list1,list2):
	if len(list1)!=len(list2):
		return False
	if ((len(list1) == 0) and (len(list2) == 0)):
		return True
	if(list1[0] != list2[0]):
		return False
	else:
		return isEqual(list1[1:],list2[1:])

print(isEqual([1,2,3,4],[1,2,3,3]))