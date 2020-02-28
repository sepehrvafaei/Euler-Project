import math
def Func(n):
    primes=[]
    arr=[True for i in range(n)]
    arr[0]=False
    arr[1]=False
    for i in range(2,int(math.sqrt(n))+1):
        if arr[i]:
            for j in range(i**2,n,i):
                arr[j]=False
    for k in range(2,n):
        if arr[k]:
            primes.append(k)
    return primes

def main():
    primes=Func(10**6)
    L=len(primes)
    sigma=0
    wanted=[]
    count=0
    i=0
    while count<40:
        if pow(10,10**9,9*primes[i])==1:
            count+=1
            sigma+=primes[i]
            wanted.append(primes[i])
        i+=1
        
    return sigma

print(main())
    

            
