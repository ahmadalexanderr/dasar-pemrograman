def copy(list1,list2):
	if len(list1) == 0:
		return list2
	else:
		list2.append(list1[0])
		return copy(list1[1:],list2)

print(copy([1,2,3,4],[]))

def copy2(list1,list2):
	if len(list1) == 0:
		return list2
	else:
		return copy2(list1[1:],list2+list1[:1])

print(copy2([1,2,3,4],[]))