def myFunc(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        primesList=[2]
        for i in range(3,n+1,2):
            isPrime=True
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    isPrime=False
                    break
            if isPrime==True:
                primesList.append(i)

    powersList=[]
    for i in primesList:
        j=1
        while i**j<n+1:
            j+=1
        powersList.append(j-1)
    
    total=1
    for i in range(len(primesList)):
        total=total*(primesList[i]**powersList[i])

    return total

print(myFunc(20))
 
            
            


    
