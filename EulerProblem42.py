import string
import math


file=open('p042_words.txt','r')

l=string.ascii_uppercase
dic={}
for i in range(26):
    dic[l[i]]=i+1

line=file.readline().strip()
line=line.replace('"','')
line=line.split(',')

count=0
for word in line:
    value=0
    for i in range(len(word)):
        value+=dic[word[i]]
    x=int(math.sqrt(2*value)) 
    if value== (x*(x+1))/2:
        count+=1

print(count)


        
