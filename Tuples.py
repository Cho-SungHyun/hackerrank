if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t=()
    
    for i in integer_list:
        lst = list(t)
        lst.append(i)
        t = tuple(lst)
        
    print(hash(t))

