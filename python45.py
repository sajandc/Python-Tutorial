x=int(input())
def fn(x):
	if(x==0):
		return 0
	else:
		return fn(x-1)+100
print(fn(x))
