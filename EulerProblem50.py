import math
import itertools

import math
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

arr=[True for i in range(10**4)]
arr[0]=False
arr[1]=False
i = 2
while (i*i <= 10**4): 
    if arr[i]: 
        for j in range(i*i, 10**4, i): 
            arr[j] = False
    i += 1

primes=[]
for i in range(2,10**4):
    if arr[i]:
        primes.append(i)


maximum=1
wanted=0
for k in range(len(primes)):
    sigma=0
    i=k
    while sigma<10*3 and i<len(primes):
        sigma+=primes[i]
        if sigma<100 and isPrime(sigma):
            if i+1>maximum:
                wanted=sigma
                maximum=i
        i+=1

print(maximum)
print(wanted)
    
    
        
