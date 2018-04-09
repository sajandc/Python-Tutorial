l1=[x for x in input().split(',')]
l2=[y for y in input().split(',')]
print(list(set(l1) ^ set(l2)))
