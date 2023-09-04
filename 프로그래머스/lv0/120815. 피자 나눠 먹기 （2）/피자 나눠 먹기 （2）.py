def solution(n):
    result=1
    for i in range(1,100,1):
        if (6*result)%n ==0:
            break
        else:
            result+=1
    
    return result