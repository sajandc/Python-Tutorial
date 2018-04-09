l=[x for x in input().split()]
for i in range(len(l)):
	print(''.join(list(reversed(l[i]))), end=" ")
