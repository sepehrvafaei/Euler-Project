def myFunc():
    a=1
    b=1
    c=0
    total=0
    order=2
    while(c<4000000):
        c=a+b
        order+=1
        if(order%3==0):
            total+=c
        a=b
        b=c
    return total

print(myFunc())
        
    
