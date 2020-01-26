from datetime import datetime as dt
def myFunc(n):
    x=n
    maxPrime=n
    while x>1:
        while x%2==0:
            maxPrime=2
            x=x/2
        i=3
        while i<x+1:
            while x%i ==0:
                maxPrime=i
                x=x/i
            i+=2
            
    return maxPrime

start=dt.now()
print(myFunc(600851475143))
finish=dt.now()
print(finish-start)

 
