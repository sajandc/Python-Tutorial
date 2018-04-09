d={}
l=[]
x=input()
l.append(x.split(' '))
for i in l:
	d[i]=d.get(i,0)+1
words=d.keys()
for w in words:
	print("%s : %d"%(w,d[w]))

