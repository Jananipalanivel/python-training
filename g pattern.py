n=5
m=n//2
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n-1 and j<m or i==m and j>m or j==m and i>=m or j==n-1 and i>m):
            print("*",end="")
        else:
            print(" ",end="")
    print()
       
