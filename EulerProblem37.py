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

wanted=[23,37,53,73,313,317,373,797]
for a in [2,3,5,7]:
    for b in[1,3,7,9]:
        if (a+b)%3 !=0:
            for c in [1,3,7,9]:
                if (a+b+c)%3 !=0:
                    for d in [3,7]:
                        if (a+b+c+d)%3 !=0:
                            if (isPrime(1000*a+100*b+10*c+d) and
                                isPrime(100*b+10*c+d) and
                                isPrime(10*c+d) and
                                isPrime(d) and 
                                isPrime(100*a+10*b+c) and
                                isPrime(10*a+b) and
                                isPrime(a)):
                                wanted.append(1000*a+100*b+10*c+d)
                                
                                
for a in [2,3,5,7]:
    for b in[1,3,7,9]:
        if (a+b)%3 !=0:
            for c in [1,3,7,9]:
                if (a+b+c)%3 !=0:
                    for d in [1,3,7,9]:
                        if (a+b+c+d)%3 !=0:
                            for e in[3,7]:
                                if (a+b+c+d+e)%3 !=0:
                                    if (isPrime(10000*a+1000*b+100*c+10*d+e) and
                                        isPrime(1000*b+100*c+10*d+e) and
                                        isPrime(100*c+10*d+e) and
                                        isPrime(10*d+e) and 
                                        isPrime(e) and
                                        isPrime(1000*a+100*b+10*c+d) and
                                        isPrime(100*a+10*b+c) and
                                        isPrime(10*a+b) and
                                        isPrime(a)):
                                        wanted.append(10000*a+1000*b+100*c+10*d+e)


for a in [2,3,5,7]:
    for b in[1,3,7,9]:
        if (a+b)%3 !=0:
            for c in [1,3,7,9]:
                if (a+b+c)%3 !=0:
                    for d in [1,3,7,9]:
                        if (a+b+c+d)%3 !=0:
                            for e in[1,3,7,9]:
                                if (a+b+c+d+e)%3 !=0:
                                    for f in[3,7]:
                                        if (a+b+c+d+e+f)%3 !=0:
                                            if (isPrime(100000*a+10000*b+1000*c+100*d+10*e+f) and
                                                isPrime(10000*b+1000*c+100*d+10*e+f) and
                                                isPrime(1000*c+100*d+10*e+f) and
                                                isPrime(100*d+10*e+f) and 
                                                isPrime(10*e+f) and
                                                isPrime(f) and
                                                isPrime(10000*a+1000*b+100*c+10*d+e) and
                                                isPrime(1000*a+100*b+10*c+d) and
                                                isPrime(100*a+10*b+c) and
                                                isPrime(10*a+b) and
                                                isPrime(a) ):
                                                    wanted.append(100000*a+10000*b+1000*c+100*d+10*e+f)


print(wanted)
total=0
for i in wanted:
    total+=i
print(total)
