#question
1 4 5 16 17 20 21 68 69 80... a infinite series. Given a number N check whether the number will be part of the series or not. If yes print the corresponding index of the number else print NOT PRESENT.
Input Format
A single integer N
Constraints
1<=N<=2^64
Output Format
If present in series print only the Index
else print "NOT PRESENT"

#answer
n=int(input())
k=bin(n)[2:]
odd=k[1::2]
if len(k)%2!=0 and int(odd)==0:
    even=k[0::2]
    print(int(even,2))
else:
    print("NOT PRESENT")
    
    
        
