# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

num = int(input())
d = deque()

for i in range(num):
    command, *n = input().split()
    exec(f'd.{command}({str(*n)})')
    
print(*d)
