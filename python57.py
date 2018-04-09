def swap_case(s):
    l=[]
    for i in range(len(s)):
        if(str(s[i]).isupper()):
            a=ord(s[i])
            l.append(chr(a+32))
        if(str(s[i]).islower()):
            a=ord(s[i])
            l.append(chr(a-32))
        else:
            l.append(s[i])
    return (''.join(l))
s=input()
result=swap_case(s)
print(result)
