def solution(price, money, count):
    
    residual=0
    for i in range(1,count+1):
        residual+=i*price
    if  money<residual:
        answer= residual-money
        
    else:
        answer = 0
        
        

    return answer