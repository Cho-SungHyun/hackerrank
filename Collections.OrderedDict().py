# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

num = int(input())
ordered = OrderedDict()

for i in range(num):
    items = input().split()
    item_name = " ".join(items[:-1])
    item_price = int(items[-1])
    if item_name not in ordered:
        ordered[item_name] = item_price
    elif item_name in ordered:
        ordered[item_name] += item_price
        
for name, price in ordered.items():
    print(name, price)
