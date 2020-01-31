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

    
def myFunc(a,b):
    n=0
    while isPrime(n**2+n*a+b):
        n+=1
    return n-1

listA=[]
listB=[]

i=-999
while i<999 :
    i+=2
    listA.append(i)

for i in range(3,1000):
    if isPrime(i):
        listB.append(i)

def main():
    largest=0
    pair=[0]
    for i in listA:
        for j in listB:
            if j>i and myFunc(i,j)>largest:
                largest=myFunc(i,j)
                pair.clear()
                pair.append(i)
                pair.append(j)

    return pair[0]*pair[1]
                
print(main())           
            
        
