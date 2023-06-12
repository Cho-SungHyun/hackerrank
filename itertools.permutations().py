# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

A, B = input().split()
array = sorted(list(permutations(A, int(B))))

for result in array:
    print("".join(result))
