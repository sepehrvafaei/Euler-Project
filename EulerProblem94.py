h=4
y=7
s=0
while True:
    '''x and x+1'''
    if (2*y+1)%3==0 and (h*(y+2))%3==0:
        if (2*y+2)>10**9:
            break
        else:
            x=(2*y+1)/3
            s+=2*y+2
    ''' x and x-1'''
    if (2*y-1)%3==0 and (h*(y+1))%3==0:
        if (2*y-2)>10**9:
            break
        else:
            x=(2*y-1)/3
            s+=2*y-2
    temp=y
    y=2*y+3*h
    h=2*h+temp

print(s)


    
