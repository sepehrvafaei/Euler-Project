def isPalindrom(n):
    l=str(n)
    return l==l[::-1]

def main():
    s=0
    for n in range(1,10**6):
        if isPalindrom(n):
            temp=format(n,'b')
            if isPalindrom(temp):
                s+=n
    return s

print(main())


     
            
        
