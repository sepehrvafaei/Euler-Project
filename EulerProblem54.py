'''High Card: Highest value card.>>>0
One Pair: Two cards of the same value.>>>1
Two Pairs: Two different pairs.>>>2
Three of a Kind: Three cards of the same value.>>>3
Straight: All cards are consecutive values.>>>4
Flush: All cards of the same suit.>>>5
Full House: Three of a kind and a pair.>>>6
Four of a Kind: Four cards of the same value.>>>7
Straight Flush: All cards are consecutive values of same suit.>>>8
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.>>>9'''
file=open('p054_poker.txt','r')
p1v=[]
p1s=[]
p2v=[]
p2s=[]
c1=0
c2=0
h1=0
h2=0
dic={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
for line in file:
    p1v=sorted([dic[line[3*i]] for i in range(5)])
    p1s={line[3*i+1] for i in range(5)}
    if len(p1s)==1:
        if min(p1v)==10:
            h1=9
        elif max(p1v)-min(p1v)+1 == 5:
            h1=8
        else:
            h1=5
    elif len(set(p1v))==2:
        if p1v[1]==p1v[2] and p1v[2]==p1v[3]:
            h1=6
        else:
            h1=7
    elif len(set(p1v))==3:
        if ((p1v[0]==p1v[1] and p1v[1]==p1v[2]) or (p1v[1]==p1v[2] and p1v[2]==p1v[3]) or
            (p1v[2]==p1v[3] and p1v[3]==p1v[4])):
            h1=3
        else:
            h1=2
    elif len(set(p1v))==4:
        h1=1
    elif ((max(p1v)-min(p1v)+1 == 5) and (p1v[0]==p1v[1]-1) and
          (p1v[1]==p1v[2]-1) and (p1v[2]==p1v[3]-1) and
          (p1v[3]==p1v[4]-1)):
        h1=4
    else:
        h1=0
'''---------------------------------------------------------------------'''
    p2v=sorted([dic[line[3*i]] for i in range(5,10)])
    p2s={line[3*i+1] for i in range(5,10)}
    if len(p2s)==1:
        if min(p2v)==10:
            h2=9
        elif max(p2v)-min(p2v)+1 == 5:
            h2=8
        else:
            h2=5
    elif len(set(p2v))==2:
        if p2v[1]==p2v[2] and p2v[2]==p2v[3]:
            h2=6
        else:
            h2=7
    elif len(set(p2v))==3:
        if ((p2v[0]==p2v[1] and p2v[1]==p2v[2]) or (p2v[1]==p2v[2] and p2v[2]==p2v[3]) or
            (p2v[2]==p2v[3] and p2v[3]==p2v[4])):
            h2=3
        else:
            h2=2
    elif len(set(p2v))==4:
        h2=1
    elif ((max(p2v)-min(p2v)+1 == 5) and (p2v[0]==p2v[1]-1) and
          (p2v[1]==p2v[2]-1) and (p2v[2]==p2v[3]-1) and
          (p2v[3]==p2v[4]-1)):
        h2=4
    else:
        h2=0
'''---------------------------------------------------------------------'''
    if h1>h2:
        c1+=1
    elif h1<h2:
        c2+=1
    else:
        if h1==0:
            for i in range(5):
                if p1v[i]>p2v[i]:
                    c1+=1
                    break
                elif p1v[i]<p2v[i]:
                    c2+=1
                    break
        elif h1==1:
            '''if p1v[2]>p2v[2]:
                c1+=1
            elif p1v[2]<p2v[2]:
                c2+=1
            else:
                if p1v[3]==p1v[4]:
                    if p2v[3]==p2v[4]:
                        if p1v[0]>p2v[0]:
                            c1+=1
                        elif p1v[0]<p2v[0]:
                            c2+=1
                    else:
                        c2+=1
                else:
                    if p2v[3]==p2v[4]:
                        c1+=1
                    else:
                        if p1v[4]>p2v[4]:
                            c1+=1
                        elif p1v[4]<p2v[4]:
                            c2+=1'''
            pass
        elif h1=2:
            pass
            
            

        
    
    
    










