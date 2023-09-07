def solution(s):
    answer=''
    
    a=sorted(s)
    a=a[::-1]
    
    for i in a:
        answer+=i
    
    return answer
#     a=[]
#     for i in s:
#         a.append(i)
        
#     answer = a.sort(reverse=True)    
#     return answer
