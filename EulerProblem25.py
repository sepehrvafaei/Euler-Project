def myFunc(n):
    a=1
    b=1
    c=0
    i=2
    m=10**(n-1)
    while c<m:
        c=a+b
        i+=1
        a=b
        b=c
    return i

print('the order of first fibonacci number with 1000 digits:')
print(myFunc(1000))
