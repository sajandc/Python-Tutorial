x=int(input())
l=[]
def fab(n):
	if(n==0):
		return 0
	elif(n==1):
		return 1
	else:
		return fab(n-1)+fab(n-2)
s=[str(fab(x)) for x in range(0,x+1)]
print(','.join(s))
