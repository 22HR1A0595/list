///
Write a program to sort the given list and print it.
Sample Input:
30 20 10 50 40
Sample Output:
10 20 30 40 50 
///
l=[]
n=int(input())
for i in range(n):
a=int(input())
l.append(a)
print(l.sort())
