import re
l=[x for x in input().split(' ')]
l1=[]
for i in l:
	if(i.isalpha()):
		l1.append(i)
print(l1)
