///
Write a program to print the given list in reverse order.
Sample Input:
10 20 30 40 50
Sample Output:
50 40 30 20 10 
///
n=int(input())
st=[]
for i in range(n):
a=int(input())
st.append(a)
print(st.sort(reverse=True))
