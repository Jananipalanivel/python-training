a=20
l=[]
for i in range(2,a):
   while(a%i==0):
       a//=i
       l.append(i)
print(*l)      
       
