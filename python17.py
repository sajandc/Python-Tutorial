lines=[]
while True:
	i=input()
	if i:
		lines.append(i)
	else:
		break
com=0
for i in lines:
	if(i[0]=='D'):
		com=com+int(i[1:])
	elif(i[0]=='W'):
		com=com-int(i[1:])
print(com)	
