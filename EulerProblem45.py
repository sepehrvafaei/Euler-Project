import math
n=144
while True:
    H=n*(2*n-1)
    if (1+math.sqrt(1+24*H)) %6 ==0:
        break
    else:
        n+=1

print(H)
        
    
    

    
        
    
    
    
    
    
