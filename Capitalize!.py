

# Complete the solve function below.
def solve(s):
    name = s.split()
    
    for i in name:
        index = s.find(i)
        cap = i[0].upper()
        s = s[:index] + cap + s[index+1:]
        
    return s


