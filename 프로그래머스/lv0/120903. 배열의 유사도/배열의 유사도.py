def solution(s1, s2):
    answer =0
    for i in s1:
        for s in s2:
            if i==s:
                answer+=1
        
    return answer