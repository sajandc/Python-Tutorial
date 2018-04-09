l=[]
d={'Upper':0,'Lower':0}
l=[x for x in input().split(' ')]
for i in l:
	for j in i:
		if(j.isupper()):
			d['Upper']+=1
		if(j.islower()):
			d['Lower']+=1
		else:
			pass
print(d)
