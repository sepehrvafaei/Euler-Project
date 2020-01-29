import math
from datetime import datetime as dt

dic={}
def sumOfDivisors(n):
  sum=0
  for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
      sum +=(i+n/i)
  if int(math.sqrt(n))**2==n:
    sum -=i
  return sum+1

for i in range(2,10000):
    dic[i]=int(sumOfDivisors(i))

def myFunc2():
  sum=0
  for i in range(2,10000):
    for j in range(i+1,10000):
      if j==dic[i] and i==dic[j]:
        sum+=(i+j)
  return sum
  
s=dt.now()
print(myFunc2())
f=dt.now()
