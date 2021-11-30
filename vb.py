def MassVote(N, Votes = []):
    sum_v = 0
    for i in range(len(Votes)):
        sum_v = sum_v + Votes[i]
    result = []
    for j in range(len(Votes)):
        r = ((((Votes[j] * 100)/ sum_v) / 0.001) // 1)*0.001
        result.append(r)
    max_win = result[0]
    if N == 1:
        str_res = "majority winner " + str(1)
    for r in range(1,len(result)):
        if max_win < result[r]:
            max_win = result[r]
            if max_win > 50:
                str_res = "majority winner " + str(r+1)
            elif max_win < 50:
                str_res = "minority winner "+ str(r+1)
        elif result.count(max_win) > 1:
            str_res = "no winner"
        elif max_win == result[0] and max_win > 50:
            str_res = "majority winner " + str(1)
        elif max_win == result[0] and max_win < 50:
            str_res = "minority winner "+ str(1)
            
    return str_res