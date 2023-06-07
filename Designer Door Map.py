# Enter your code here. Read input from STDIN. Print output to STDOUT

r,c = map(int,input().split())


pat = [('.|.'*(2* i +1)).center(c,'-') for i in range(r//2)]
print('\n'.join(pat + ['WELCOME'.center(c,'-')] + pat[::-1]))

