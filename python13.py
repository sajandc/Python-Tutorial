l=[]
l=[x for x in input().split(' ')]
d={'letter':0,'digit':0}
for i in l:
	for j in i:
		if(j.isdigit()):
			d['digit']+=1
		if(j.isalpha()):
			d['letter']+=1
		else:
			pass
print(d)
