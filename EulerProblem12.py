import math
def myFunc(n):
    j=2
    while True:
        a=(j*(j+1))/2
        j+=1
        factors=0
        for i in range(1,int(math.sqrt(a))):
            if a%i==0:
                factors+=2
        if factors >n:
            break
    return a
        
print(myFunc(500))            
