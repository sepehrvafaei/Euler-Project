from itertools import combinations
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

nums=[True for i in range(1000)]
nums[0]=False
nums[1]=False
for i in range(2,int(math.sqrt(1000))+1):
    if nums[i]==True:
        for j in range(i**i,1000,i):
            nums[j]=False
primes=[i for i in range(1000) if nums[i]==True]
length=len(primes)
for i in range(length):
    for j in range(i+1,length):
        for k in range(j+1,length):
            for z in range(k+1,length):
                for q in range(z+1,length):
                    
                    '''temp=True
                    for j in range(5):
                        for k in range(j+1,5):
                            if (i[j]+i[k])%3==0:
                                temp=False
                                break
                    if temp:
                        for a in range(5):
                            for b in range(a+1,5):
                                if (isPrime(int(str(a)+str(b))) and isPrime(int(str(b)+str(a)))) ==False:
                                    temp=False
                                    break
                    if temp:
                        sigma=0
                        for c in range(5):
                            sigma+=i[c]
                            
                        print(i)
                        print(sigma)
                        break'''
                    

            
    
