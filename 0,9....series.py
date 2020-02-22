n=int(input())
k=1
while(int(bin(k).replace("1","9")[2:])%n!=0):
    k+=1
print(bin(k).replace("1","9")[2:])
#output
42
90090
