x=input()
d={}
for i in range(len(x)):
	d[x[i]]=d.get(x[i],0)+1
print('\n'.join(sorted('%s - %s '%(v,k) for v,k in d.items())))
print(sorted(d.items(), key=lambda d: d[1]))
