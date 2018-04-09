l=[]
l=[x for x in input().split(',')]
def missing(l):
	l1=[]
	l2=[]
	for j in range(len(l)):
		l2.append(int(l[j]))
	l1=[i for i in range(int(l[0]),int(l[-1])+1)]	
	print(list(set(l1) ^ set(l2)))
missing(l)
