import re
l=[]
l1=[]
l=[x for x in input().split(',')]
c=0
for i in l:
	if(len(i)<6 or len(i)>12):
		pass
	else:
		if not re.search("[a-z]",i):
			continue
		elif not re.search("[A-Z]",i):
			continue
		elif not re.search("[0-9]",i):
			continue
		elif not re.search("[$#@]",i):
			continue
		else:
			pass
		l1.append(i)
print(l1)


