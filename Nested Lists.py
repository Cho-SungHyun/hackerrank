if __name__ == '__main__':
    newlist=[]
    scorelist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        newlist.append([name, score])
        scorelist.append(score)
    newlist.sort(key = lambda x:(x[1], x[0]))
    scorelist = list(set(scorelist))
    scorelist.sort()
    
    for i in range(len(newlist)):
        if scorelist[1] == newlist[i][1]:
            print(newlist[i][0])
    

