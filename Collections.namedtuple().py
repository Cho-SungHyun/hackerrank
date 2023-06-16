# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

num = int(input())
STUDENT = namedtuple('STUDENT', input().split())
marks = []

for i in range(num):
    marks.append(float(STUDENT(*input().split()).MARKS))
print(sum(marks)/num)
