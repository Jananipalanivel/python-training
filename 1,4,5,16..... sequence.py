n=int(input())
c=0
s=0
while(n):
    if(n&1):
        s=s+4**c
    c+=1
    n=n>>1
print(s)
#answer2
n=int(input())
s=bin(n)[2:]
j=" "
for i in range(0,len(s)):
    if i%2==0:
        j+=s[i]       
a=int(j,2)
if n==int(j,4):
    print(a)
else:
    print("NOT PRESENT")
