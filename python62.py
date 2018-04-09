import re
x=int(input())
l=[]
i=0
while len(l)<x :
	i=i+1
	if(not re.search("[4-9]",str(i))):
		if(not re.search("[0]",str(i))):
			l.append(i)
#print(l)
print(len(str(l[x-1])))
	
