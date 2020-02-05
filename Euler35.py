from itertools import permutations
import math
from datetime import datetime as dt

def isPrime(n):
    if n==1:
        return False
    elif n<=0:
        return False
        
    else:
        temp=True
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                temp=False
                break
        return temp

wanted=[]

def myFunc(n):
    for permu in list(permutations([1,3,7,9],n)):
        i=0
        for ip in range(n):
            i += (10**(n-1-ip))*permu[ip]
        if isPrime(i):
            arr=str(i)
            temp=True
            L=len(arr)
            for k in range(1,L):
                num=0
                for h in range(L):
                    index=(h+k)%L
                    num+=int(arr[index])*(10**(L-1-index))
                if isPrime(num) is False:
                    temp==False
                    break
            if temp==True:
                wanted.append(i)

s=dt.now()
for  i in range(2,7):
    myFunc(i)

print(wanted)
print(len(wanted))
f=dt.now()
print(f-s)
