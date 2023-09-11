# def solution(s):
#     global answer
#     for i in s:
#         if type(i)==int:
#             if (len(s)==4 or len(s)==6) :
#                 answer= true
#     return answer

def solution(s):

    if (len(s) == 4 or len(s) == 6) and s.isdigit():

        return True

    else:

        return False