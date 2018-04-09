import math
l1=[]
l=[x for x in input().split(',')]
for i in l:	
	num=int(i[0])*pow(2,3)+int(i[1])*pow(2,2)+int(i[2])*pow(2,1)+int(i[3])*pow(2,0)
	if(num%5==0):
		l1.append(i)
print(','.join(l1))

