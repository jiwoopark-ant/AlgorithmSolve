def multiply(num_list):
    ans = 1
    for n in num_list:
        if n == 0:
            return 0
        ans *= n
    return ans



def solution(num_list):
    if multiply(num_list) < sum(num_list)*sum(num_list):
        return 1
    if multiply(num_list) > sum(num_list)*sum(num_list):
        return 0
    
    