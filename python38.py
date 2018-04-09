l=[int(x) for x in input().split(',')]
print(list(filter(lambda y: y%2==0,(list(map(lambda x: x**2,l))))))
