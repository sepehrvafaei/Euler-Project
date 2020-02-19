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

n=4
while True:
    y=2*n+1
    if isPrime(y)==False:
        temp=False
        for x in range(1,int(math.sqrt(y/2))+1):
            if isPrime(y-2*(x**2)):
                temp=True
                break
        if temp==False:
            print(y)
            break
        else:
            n+=1
    else:
        n+=1
