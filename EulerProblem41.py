from itertools import permutations
import math

def isPrime(n):
    if n==1:
        return False
    else:
        temp=True
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                temp=False
                break
        return temp


def main():
    largest=0
    nums=list(permutations([1,2,3,4,5,6,7]))
    for p in nums:
        x=0
        for i in range(len(p)):
            x+=(10**(len(p)-1-i))*p[i]
        if isPrime(x):
            if x>largest:
                largest=x

    nums=list(permutations([1,2,3,4]))
    for p in nums:
        x=0
        for i in range(len(p)):
            x+=(10**(len(p)-1-i))*p[i]
        if isPrime(x):
            if x>largest:
                largest=x

    return largest

print(main())
    
