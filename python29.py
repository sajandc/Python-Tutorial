import math
x=input()
y=math.sqrt(int(x))
res=y-int(y)
if(res < 1 and res > 0):
	print('its not the sqrt of any integer')
else:
	print('%s is sqrt of %d'%(x,y))

