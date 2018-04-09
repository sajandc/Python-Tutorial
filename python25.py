x=input()
n=input()
def power_of_n(x,i,n):
	if(x>n**i):
		power_of_n(x,i+1,n)
	elif(x==n**i):
		print('%d to the power %d'%(n,i))
	else:
		print('%d is NOT power of %d'%(x,n))

power_of_n(int(x),1,int(n))
