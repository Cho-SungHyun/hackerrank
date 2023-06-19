# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())

# for i in range(1, a+1):
    # lst = []
    # for j in range(1, i+1):
    #     lst.append(str(j))
    #     if j == i and j != 1:
    #         for l in range(j-1, 0, -1):
    #             lst.append(str(l))
    # print("".join(lst))
    
for i in range(a):
    print(((((10**i) // 9) * 10) + 1)**2)
