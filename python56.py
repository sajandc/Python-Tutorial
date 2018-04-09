l=[int(x) for x in input().split()]
l1=[i for i in range(1,l[0]+1) if l[0]%i==0 and l[1]%i==0]
print(len(l1))

