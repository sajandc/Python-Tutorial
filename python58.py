x=input()
y=input()
d={}
def count_substring(x,y):
	for i in range(len(x)):
		for j in range(i+1,len(x)+1):
			yield(x[i:j])
for i in count_substring(x,y):
	d[i]=d.get(i,0)+1
print(d[y])
