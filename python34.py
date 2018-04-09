x=input()
y=int(x)
l=[]
l1=[]
while(y>0):
	l.append(y%2)
	y=int(y/2)
for i in range(0,32-len(l)):
	l.append(0)
s=0
for j in reversed(range(0,32)):
	s=s+(int(l[31-j])*(2**j))
print(s)


