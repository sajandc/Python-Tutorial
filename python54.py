x=input()
l=[int(y) for y in input().split()]
s=sum(l)
l1=sorted(l)
l2=[]
print(l1)
for i in range(int(x)):
	l2.append(int(l1[i]*int(x)))
for i in range(int(x)):
	if(l2[i]>s)
		print(l1[i])
		break

