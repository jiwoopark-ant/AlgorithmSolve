# def solution(rsp):
#     answer = ''
#     temp=''
#     for i in rsp:
#         if i == '2':
#             a=i.replace('2','0')
#             temp+a
#         elif i == '0':
#             a=i.replace('0','5')
#             temp+a
#         elif i == '5':
#             a=i.replace('5','2')
#             temp+a    
            
#     return temp
def solution(rsp):
    answer = ''
    for s in rsp:
        if s == '0':
            answer += '5'
        elif s == '2':
            answer += '0'
        elif s == '5':
            answer += '2'
    return answer