l=[int(x) for x in input().split(',')]
even=filter(lambda y: y%2==0,l)
print(list(even))
