import re
emailAddress =input()
pat2 = "(\w+\@)+(\w+)\.(com)"
#print(pat2)
r2 = re.match(pat2,emailAddress)
print(r2.group(2))
