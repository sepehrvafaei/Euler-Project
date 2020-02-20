from itertools import permutations,combinations

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

arr=list(combinations(list(range(10)),4))
l=[]
for i in arr:
    temp=[]
    var=False
    l=list(permutations(list(i)))
    num=0
    for j in l:
        if j[0]!=0:
            num=j[0]*10**3+j[1]*10**2+j[2]*10+j[3]
            if isPrime(num):
                temp.append(num)
                if len(temp)==3 and temp[1]-temp[0]==temp[2]-temp[1]:
                    var=True
                    break
    if var==True:
        break
        print(temp)
