if __name__ == '__main__':
    s = input()
    l=['False','Flase','False','False']
    print(s.isalnum())
    for i in range(len(s)):
        if(s[i].isalpha()):
            l[0]='True'
            if(s[i].isupper()):
                l[2]='True'
            else:
                l[3]='True'
        elif(s[i].isdigit()):
            l[1]='True'
    print('\n'.join(l))

