# # Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

A, B = input().split()

for i in range(1, int(B)+1):
    array = list(list(combinations(sorted(list(A)), i)))
    for result in array:
        print("".join(result))
