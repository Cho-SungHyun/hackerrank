# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

X = int(input())
shoes_list = list(map(int, input().split(" ")))
N = int(input())
total_price = 0

for i in range(N):
    d_size, price = map(int, input().split())
    if d_size in shoes_list:
        total_price += price
        shoes_list.remove(d_size)

print(total_price)
