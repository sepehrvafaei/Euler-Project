import math
def myFunc():
    for i in range(1,998):
        for j in range(i+1,998):
            if i+j+ math.sqrt(i**2+j**2)==1000:
                return i*j*(1000-i-j)

print(myFunc())
