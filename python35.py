l=[x for x in input().split(',')]
s=0
a=0
s1=0
s=int(l[1])-int(l[0])
for i in range(len(l)-1):
	s1=int(l[i+1])-int(l[i])
	if(s1!=s):
		a=1
if(a==1):
	print('Not in AP')
else:
	print('AP')
