from datetime import datetime as dt
def myFunc():
    dic={1:0}
    maximum=0
    largest=1
    for n in range(2,1000000):
        k=n
        c=0
        while k >=n:
            if k%2==0:
                k=k/2
                c+=1
            else:
                k=3*k+1
                c+=1
        c=c+dic[k]
        if c>maximum:
            maximum=c
            largest=n
        dic[n]=c
            
    return largest
s=dt.now()
print(myFunc())            
f=dt.now()
print(f-s)








