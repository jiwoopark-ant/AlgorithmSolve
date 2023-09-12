def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i==0:
            answer.append(arr[i])
        elif arr[i]!=arr[i-1]:
            answer.append(arr[i])
        
    return answer
#     for i in arr:
#         answer.append(i)
    
#     for i in range(1,len(answer)+1):
#         if answer[i] != answer[i-1]:
#             del answer[i]
        
#     return answer
    
