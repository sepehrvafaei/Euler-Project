from math import sqrt
from datetime import datetime as dt

def isPrime(n):
    temp=True
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            temp=False
            break
    return temp

s=dt.now()

wanted=[2,5]
for i in range(2,10**6):
    if isPrime(i):
        arr=list(str(i))
        for item in range(len(arr)):
            arr[item]=int(arr[item])
        temp=True
        for j in arr:
            if j in [0,2,4,5,6,8]:
                temp=False
                break
        if temp==False:
            continue
        else:
            L=len(arr)
            for k in range(1,L):
                num=0
                power=L
                for h in range(L):
                    index=(k+h)%L
                    power-=1
                    num+=arr[index]*(10**(power))
                if isPrime(num)==False:
                    temp=False
                    break
            if temp==True:
                wanted.append(i)



print(len(wanted))
f=dt.now()
print(f-s)
                    





                
                    
                
                    
            
