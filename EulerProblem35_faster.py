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

digits=[1,3,7,9]
wanted=[2,3,5,7]
for a in digits:
    for b in digits :
        if isPrime(10*a+b):
            arr=[a,b]
            temp=True
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
                wanted.append(10*a+b)
                

for a in digits:
    for b in digits:
        for c in digits:
            if isPrime(100*a+10*b+c):
                arr=[a,b,c]
                temp=True
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
                        wanted.append(100*a+10*b+c)
                    
for a in digits:
    for b in digits:
        for c in digits:
            for d in digits:
                if isPrime(1000*a+100*b+10*c+d):
                    arr=[a,b,c,d]
                    temp=True
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
                            wanted.append(1000*a+100*b+10*c+d)

for a in digits:
    for b in digits:
        for c in digits:
            for d in digits:
                for e in digits:
                    if isPrime(10000*a+1000*b+100*c+10*d+e):
                        arr=[a,b,c,d,e]
                        temp=True
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
                                wanted.append(10000*a+1000*b+100*c+10*d+e)

for a in digits:
    for b in digits:
        for c in digits:
            for d in digits:
                for e in digits:
                    for f in digits:
                        if isPrime(100000*a+10000*b+1000*c+100*d+10*e+f):
                            arr=[a,b,c,d,e,f]
                            temp=True
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
                                    wanted.append(100000*a+10000*b+1000*c+100*d+10*e+f)


print(len(wanted))
f=dt.now()
print(f-s)


    
