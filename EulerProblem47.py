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

arr=[]
for i in range(300,10000):
    if numOfDistinctPrimeFactors(i)==4:
        arr.append(i)

print(arr)
        
                

