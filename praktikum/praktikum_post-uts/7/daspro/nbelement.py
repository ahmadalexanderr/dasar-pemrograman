def nbelement(list):
	if len(list) == 0:
		return 0
	if len(list) > 0:
		return 1 + nbelement(list[1:])

print(nbelement([1,2,3,4]))