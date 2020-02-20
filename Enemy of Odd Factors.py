#question
Given a number N, Check whether the given number is enemy of Odd factor or not. A number is said to be enemy of odd factors if the number itself shoud not have odd number of factors and none of the factors (excluding 1) should have odd number of factors, If so then print "Enemy of Odd Factor" else print "Friend of Odd Factor".
Input Format
One single integer N
Constraints
1<=N<=10^9
Output Format
Enemy of Odd Factor / Friend of Odd Factor

#answer1
from math import sqrt as s
n=int(input())
flag=0
if (s(n)%1!=0):
    for i in range(2,n):
        if(n%1==0 and s(i)%1==0):
            flag=1
            break
else:
    flag=1
if flag==1:
    print("Friend of Odd Factor")
else:
    print("Enemy of Odd Factor")
