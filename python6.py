import math
values=[]
x=input()
items=x.split(',')

for i in items:
	values.append(str(round(math.sqrt(2*50*int(i)/30))))
	#values.append(str(int(round(math.sqrt(2*50*float(i)/30)))))
print(','.join(values))
