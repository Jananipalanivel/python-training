a=input()
while a!=a[::-1]:
  a=int(a)+int(a[::-1])
  a=str(a)
print(a)


#question
Given a number N, reverse and add the number till the number is a palindrome. If the number itself is a palindrome print the number itself as the output.
Input Format
One integer Value N
Constraints
1<=N<=10^9
Output Format
The palindrome number got by reversing and adding the number
Sample Input 0
123
Sample Output 0
444
Explanation 0
123 + 321 = 444
