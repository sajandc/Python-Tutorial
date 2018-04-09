l=[]
for i in range(2000,3200):
	if(i%7==0):
		if(i%5!=0):
			l.append(str(i))
print(l)
print(','.join(l))
	
