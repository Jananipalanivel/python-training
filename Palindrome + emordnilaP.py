a=input()
while a!=a[::-1]:
  a=int(a)+int(a[::-1])
  a=str(a)
print(a)
