l=[]
while True:
	s=input()
	if s:
		l.append(tuple(s.split(",")))
	else:
		break
print(sorted(l))
