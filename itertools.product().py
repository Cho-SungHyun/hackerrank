# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

for result in list(product(A, B)):
    print(f"({result[0]}, {result[1]})", end=' ')
