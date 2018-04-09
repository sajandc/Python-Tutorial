l=[int(x) for x in input().split(',')]
def bin_search(l,n,le):
	if(n>l[int(le/2)-1]):
		l=l[int(le/2):]
		le=len(l)
		#print(le)
		bin_search(l,n,le)
	elif(n<l[int(le/2)]):
		l=l[:int(le/2)]
		le=len(l)
		#print(le)		
		bin_search(l,n,le)
	else:
		print(le)
le=len(l)
n=int(input())
bin_search(l,n,le)
