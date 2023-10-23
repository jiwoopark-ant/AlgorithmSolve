def solution(my_string, num1, num2):
    
    # b=[]
    # for i in my_string:
    #     if my_string.index(i)==num1:
    #         b.append(i)
    #     elif my_string.index(i)==num2:
    #         b.append(i)    
    # print(b)        
    # return answer
    s=list(my_string)
    s[num1],s[num2]=s[num2],s[num1]
    return "".join(s)