# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

A, B = input().split()

array = list(combinations_with_replacement(sorted(list(A)), int(B)))

for result in array:
    print("".join(result))
