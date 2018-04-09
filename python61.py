x=int(input())
l=[int(y) for y in input().split(' ')]
z=int(input())
l1=[int(w) for w in input().split(' ')]
l2=sorted(l)
for j in range(len(l1)):
	s=0
	for i in range(len(l)):
		s=s+l2[i]
		if(s>l1[j]):
			print(i)
			break
