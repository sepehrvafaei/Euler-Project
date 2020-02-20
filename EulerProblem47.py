import math
def numOfDistinctPrimeFactors(n):
    count=0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            count+=1
            while n%i==0:
                n=n/i

    if n!=1:
        count+=1

    return count

c=1
f=2*3*5*7
while c<4:
    f+=1
    if numOfDistinctPrimeFactors(f)==4:
        c+=1
    else:
        c=0

print(f-3)
