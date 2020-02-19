n=int(input())
a=list(map(int,input().split()))
k=n-1 if n%2!=0 else n
for i in range(0,k-1,2):
    a[i],a[i+1]=a[i+1],a[i]
print(*a)
