import math
a=int(input())
b,c=map(int,input().split())
d=int(input())
s=abs(b-c)
dis1=a*math.sqrt(2)
dis2=math.sqrt(d)*math.sqrt(2)
dis=dis1-dis2
t=dis/s
print(t)
