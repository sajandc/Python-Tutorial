def fun():
	d={}
	for i in range(1,4):
		d[i]=i*i
	print(d.items())
	for (k,v) in d.items():
		print(k,v)
fun()
