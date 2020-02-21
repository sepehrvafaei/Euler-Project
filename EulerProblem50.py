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
start=0
for k in range(len(primes)):
    sigma=primes[k]
    i=k+1
    count=1
    temp=sigma
    while sigma<10**6 and i<len(primes):
        sigma+=primes[i]
        if sigma<10**6 and isPrime(sigma):
            count=(i+1)-k
            temp=sigma
        i+=1
    if count>maximum:
        maximum=count
        wanted=temp
        start=k
        

print('number of consecutive primes in summation: ',maximum)
print('prime sum: ',wanted)
print('starting prime number in summation: ',primes[start])
