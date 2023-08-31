def solution(num, n):
    if num % n == 0:
        answer = 1
    if num % n !=  0:
        answer = 0
    return answer