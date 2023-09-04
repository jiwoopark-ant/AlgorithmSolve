def solution(balls, share):
    sol1=1
    sol2=1
    sol3=1
    for i in range(1,balls+1,1):
        sol1*=i
    for i in range(1,share+1,1):
        sol2*=i
    for i in range(1,balls-share+1,1):
        sol3*=i
        
        
    return sol1/(sol2*sol3)