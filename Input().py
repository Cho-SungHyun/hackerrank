# Enter your code here. Read input from STDIN. Print output to STDOUT

x, k = input().split()

result = eval(input().replace("x", x))

print(result == int(k))
