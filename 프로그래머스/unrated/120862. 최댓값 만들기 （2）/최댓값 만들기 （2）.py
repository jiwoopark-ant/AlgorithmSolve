from itertools import permutations
def solution(numbers):
    numbers.sort()
    return(max(numbers[0]*numbers[1],numbers[-1]*numbers[-2]))
    
    
#     for i in numbers:
#         for j in range(1,len(numbers)+1):
#             answer.append(i*j)
#     print(answer)        
    
#     a= max(answer)
#     return a
