# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

num = int(input())
dist = 0
lst = OrderedDict()

for i in range(num):
    words = input()
    if words not in lst:
        lst[words] = 1
        dist += 1
    elif words in lst:
        lst[words] += 1
        
print(dist)
for results in lst.values():
    print(results, end=" ")
