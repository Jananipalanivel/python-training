n=5
m=n//2
for i in range(n):
    for j in range(n):
        if(j==0 or j==n-1 or i<=m and i==j or i<=m and i+j==n-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
       