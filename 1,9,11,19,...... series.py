#answer
le,i=1,0
l=[]
for _ in range(100):
    s=bin(i)[2:]
    s=s.zfill(le)
    s=s.replace("1","9")
    s=s.replace("0","1")
    l.append(s)
    print(s)
    i+=1
    if (i==2**le):
        le+=1
        i=0
#answer 2
n = int(input())
fill = 1
k = 0
p = 2
c = 1
while(n):
    g = bin(k)[2:]
    g = g.zfill(fill)
    g = g.replace('1','9')
    g = g.replace('0','1')
    print(g)
    k+=1
    c+=1
    if(c>p):
        k = 0
        p*=2
        fill+=1
        c = 1
    
    n-=1
