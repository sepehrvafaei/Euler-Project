from datetime import datetime as dt
import math
def myFunc(n):
    if n==1:
        return 0
    else:
        total=2
        for i in range(3,n+1,2):
            isPrime=True
            for j in range(2,int(math.sqrt(i))+1):
                if i%j==0:
                    isPrime=False
                    break
            if isPrime==True:
                total+=i
        return total

start=dt.now()
print(myFunc(2000000))
finish=dt.now()
print(finish-start)
