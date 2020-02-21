n = int(input())
l = n
r = n
for i in range(n):
    for left in range(i,0,-1):
        print(l,end="")
        l-=1
    for j in range(2*r-1):
            print(r,end="")
    r-=1
    for right in range(i,0,-1):
        print(l+1,end="")
        l+=1
    print()
for i in range(1,n):
    for b_left in range(i,n):
         print(l,end="")
         l-=1
    for b_middle in range(2*i-1):
        print(l+1,end="")
    for b_right in range(i,n):
        print(l+1,end="")
        l+=1
    print()
    
        
