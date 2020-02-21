i=2
temp=False
while True:
    for j in range(10**i-1,(10**i)*2,3):
        if (('5' in str(j)) and ''.join(sorted(str(j)))==''.join(sorted(str(2*j))) and
            ''.join(sorted(str(2*j)))==''.join(sorted(str(3*j))) and
            ''.join(sorted(str(3*j)))==''.join(sorted(str(4*j))) and
            ''.join(sorted(str(4*j)))==''.join(sorted(str(5*j))) and
            ''.join(sorted(str(5*j)))==''.join(sorted(str(6*j)))):
            temp=True
            print(j)
            break
    if temp:
        break
    i+=1

        
        
