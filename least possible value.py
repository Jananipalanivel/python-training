#answer1
a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
l4=[]
l5=[]
for i in range(len(l2)):
    l3.append(abs(l2[i]))
c=max(l3)
d=l3.index(c)
if l2[d]<0:
    e=l1[d]+(b*2)
else:
    e=l1[d]+(b*-2)
for i in range(len(l1)):
    l4.append(str(l1[i]))
l1[d]=e
for i in range(len(l1)):
    g=l1[i]*l2[i]
    l5.append(g)
print(sum(l5))
