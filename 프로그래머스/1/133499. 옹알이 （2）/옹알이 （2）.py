def solution(babbling):
    answer=0
    #가능 옹알이 
    possible=['aya','ye','woo','ma']
    impossible=['ayaaya','yeye','woowoo','mama']
    
    for i in babbling:
        while i:
            if i[:2] in possible and i[:4] not in impossible:
                i=i[2:]
            elif i[:3] in possible and i[:6] not in impossible:
                i=i[3:]
            else:
                break
             
        if not i:
            answer+=1
    
    return answer