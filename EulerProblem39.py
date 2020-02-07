import math
from datetime import datetime as dt
def myFunc(n):
    count=0
    for a in range(int(n/2),1,-1):
        for b in range(1,a):
            if (n-a-b)>b and (n-a-b)<a:
                if a**2==b**2+(n-a-b)**2:
                    count+=1

    for a in range(int(n/2),int(math.sqrt(2)*n/2)):
        for b in range(1,int(n/2)):
            if (n-a-b)>b and (n-a-b)<int(n/2):
                if (n-a-b)**2+b**2==a**2:
                    count+=1

    return count
    

def main():
    largest=0
    p=0
    for i in range(1,1000):
        temp=myFunc(i)
        if temp>largest:
            largest=temp
            p=i
    return p

s=dt.now()
print(main())
f=dt.now()
print(f-s)
    
    


    
    
