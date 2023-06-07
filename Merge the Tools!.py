def merge_the_tools(string, k):
    # your code goes here
    chunk = len(string)/k
    ls1 = []
    ls2 = []
    index = 0
    
    for i in range(0, len(string), k):
        result = ""
        ls1.append(string[i:i+k])
        temp = list(set(ls1[index]))
        
        for j in range(len(temp)):
            result += temp[j]
        
        print(result)
        index += 1

