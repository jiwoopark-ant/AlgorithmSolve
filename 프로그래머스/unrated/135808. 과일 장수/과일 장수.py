def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    
    for i in range(0,len(score),m): #range(start,end,step)
        box=score[i:i+m]
        
        if len(box)==m: #박스크기 확인+가격
            answer+=min(box)*m
    
    
    return answer