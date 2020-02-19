n=int(input())
b=str(n)
if b[0]=="-":
    a="-"+str(int(b[1:][::-1]))
    print(a)
else:
    a=int(b[::-1])
    print(a)
