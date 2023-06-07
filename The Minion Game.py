def minion_game(string):
    # your code goes here
    s_score = 0
    k_score = 0
    string = string.upper()
    s = len(string)
    win = ""
    for i in range(s):
        if string[i] in 'AEIOU':
            k_score += (s-i)
        else:
            s_score += (s-i)
    if s_score > k_score :
        win = "Stuart " + str(s_score)
    elif k_score > s_score :
        win = 'Kevin ' + str(k_score)
    else :
        win = 'Draw'
    print(win)
    return win


