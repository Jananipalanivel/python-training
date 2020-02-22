n=5
m=n//2
for i in range(n):
    for j in range(n):
        if(i==m or j==m or j==0 and  i<m or i==n-1 and j<m or j==n-1 and i>m or i==0 and j>m):
            print("*",end="")
        else:
            print(" ",end="")
    print()
     
