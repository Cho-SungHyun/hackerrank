# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

A,B = map(int, input().split())
g_A, g_B = [], []

for a in range(A):
    g_A.append(input())
for b in range(B):
    g_B.append(input())
    
for index1 in g_B:
    if index1 not in g_A:
        print("-1")
    else:
        indices = []
        for index2, value in enumerate(g_A):
            if index1 == value:
                indices.append(str(index2+1))
            # break
        print(" ".join(indices))
