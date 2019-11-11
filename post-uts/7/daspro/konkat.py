def konkat(list1,list2):
	if len(list2)==0:
		return list1
	else:
		return konkat(list1+list2[:1],list2[1:])

print(konkat([1,2,3,4],[5,6,7]))