import operator
l=[x for x in input().split(',')]
d={}
for i in l:
	d[i]=d.get(i,0)+1
sorted_list=sorted(d.items(),key=operator.itemgetter(0))
l1=[]
for j in sorted_list:
	if(j[1]==2):
		l1.append(j[0])	
print(','.join(l1))
print(sorted_list)

