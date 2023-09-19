def solution(t, p):
    answer = 0
    b=len(p)
    for i in range(len(t)-b+1): # range 조정 필수
        if int(t[i:i+b])<=int(p):
            answer+=1
    return answer