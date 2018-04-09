x=input()
y=x.split(',')
r=int(y[0])
c=int(y[1])
multilist=[[0 for i in range(c)]for j in range(r)]

for i in range(int(r)):
	for j in range(int(c)):
		multilist[i][j]=i*j
print(multilist)
