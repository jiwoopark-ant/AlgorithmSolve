
# def prime(n):
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#         # else:
#         #     return True
#         return True
# def solution(n):
#     answer=0
#     for i in range(2,n+1):
#         if prime(i)==True:
#             answer+=1
#     return answer

import math
def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(2, n+1):
        if prime(i) == True:
            answer += 1
    return answer