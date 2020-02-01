from datetime import datetime as dt
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

def myFunc(n):
    pair=[]
    for i in range(2,int(math.sqrt(n))+1):
        for j in range(2,int(math.log(n,10)/math.log(2,10))+1):
            if i**j==n:
                pair.append(i)
                pair.append(j)
                return pair[0]


dic={}
for i in range(2,101):
    if myFunc(i)== None:
        dic[i]=[]
        for j in range(2,101):
            dic[i].append(i**j)
        

def main(n):
    nums=list(range(2,n+1))
    distinct=[]
    limit=n**n
    for i in nums:
        if isPrime(i):
           for j in nums:
                    distinct.append(i**j) 

        elif myFunc(i)==None:
            for j in nums:
                    distinct.append(i**j)
        else:
            for j in nums:
                if i**j not in dic[myFunc(i)] and i**j not in distinct:
                    distinct.append(i**j)
            
    return len(distinct)

s=dt.now()
print(main(200))
f=dt.now()
print(f-s)
            
            

            
            
