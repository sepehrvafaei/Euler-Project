import os
import string
def main():
    values=dict(zip(string.ascii_uppercase, range(1,27)))
    file=open('p022_names.txt','r')
    s=file.read()
    s=s.split(',')
    for i in range(len(s)):
        s[i]=s[i].strip('''"''')
    s.sort()
    sigma=0
    for i in range(len(s)):
        temp=0
        for j in range(len(s[i])):
            temp += values[s[i][j]]

        sigma += (i+1)*temp
    return sigma
            
print(main())
    
    
