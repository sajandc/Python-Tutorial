x=input()
def digit(x):
	s=0	
	for i in range(len(x)):
		s=s+int(x[i])	
	if(len(str(s))>1):
		digit(str(s))
	else:	
		print(s)
digit(x)




