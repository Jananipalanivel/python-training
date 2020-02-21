n1=list(input())
n2=list(input())
for i in n1:
    if i in n2:
        n1.remove(i)
        n2.remove(i)
k=len(n1)+len(n2)
l=['F','L','A','M','E','S']
while(len(l)>1):
    if k%len(l)==0:
        l=l[:-1]
    else:
        m=k%len(l)
        left=l[:m-1]
        right=l[m:]
        l=right+left
print(l[0])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    
