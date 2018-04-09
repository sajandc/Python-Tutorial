import math
l=[]
while True:
	x=input()
	if x:
		l.append(x.split(" "))
	else:
		break
step1=0
step2=0
for i in l:
	if(i[0]=='UP'):
		step1=step1+int(i[1])
	elif(i[0]=='DOWN'):
		step1=step1-int(i[1])
	elif(i[0]=='LEFT'):
		step2=step2+int(i[1])
	elif(i[0]=='RIGHT'):
		step2=step2-int(i[1])
com=round(math.sqrt((step1*step1)+(step2*step2)))
print(com)


