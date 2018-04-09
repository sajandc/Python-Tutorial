l=[]
for x in range(1000,3000):
	j=str(x)
	if((int(j[0])%2==0) and (int(j[1])%2==0) and (int(j[2])%2==0) and (int(j[3])%2==0)):
		l.append(j)
print(','.join(l))

