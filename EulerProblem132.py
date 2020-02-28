def Repunit(n):
    s=0
    for i in range(n):
        s+=10**i
    return s

import math
def numOfDistinctPrimeFactors(n):
    l=[]
    for i in range(2,int(n/2)+1):
        if n%i==0:
            l.append(i)
            while n%i==0:
                n=n/i
    if len(l)==0:
        l.append(n)
    return l

arr=[]
arr_2=numOfDistinctPrimeFactors((10**100-1)//(10**10-1))
for i in arr_2:
    arr.append(i)

n=1
while True:
    var=False
    temp=numOfDistinctPrimeFactors(10**n)
    if len(arr)==40:
        var=True
        break   
    for i in temp:
        if i not in arr:
            if len(arr)==40:
                var=True
                break
                arr.append(i)
    if var:
        break
    n+=1

print(arr)
    
    


    
