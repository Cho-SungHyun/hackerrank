# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int,input().split())
arr = set(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
print(len(A.intersection(arr))-len(B.intersection(arr)))
