import math
def lcm(a,b):
    c=math.gcd(a,b)
    d=a//c
    f=b//c
    return c*d*f
    
def solution(n, m):
    answer = [math.gcd(n,m), lcm(n,m)]
    return answer