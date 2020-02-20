#question
Sivasamy is a farmer living in the southern part of Tamilnadu. He has ‘N’ bulls on his farm, which he uses to plough his fields. Hence “Mattu Pongal” is a special occasion to celebrate the hard work of all those bulls. So, for every Mattu Pongal, the bulls will be decorated, the horns of the bull are painted. Each bull is painted with different colors so it looks visually appealing. But seeing the cost-effectiveness part, it is difficult to buy ‘N’ different colors of paints. So Sivasamy usually mixes two or more colors to make a newer color. Paintbox costs 225 rs each. So what will be the minimum expenditure of Sivasamy to color all his ‘N’ bulls with different colors?
Input Format
One single integer input N – Number of bulls
Constraints
1<=N<=10^9
Output Format
One single integer output denoting the minimum expenditure of Sivasamy.
Sample Input 0
7430427
Sample Output 0
5175
#answer
n=int(input())
print(n.bit_length()*225)



