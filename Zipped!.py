# Enter your code here. Read input from STDIN. Print output to STDOUT

N, X = map(int, input().split())
lst = []

for i in range(X):
    lst.append(input().split(" "))

for i in range(N):
    avg = 0
    for j in range(X):
        avg += float(lst[j][i])
    print(avg/X)
