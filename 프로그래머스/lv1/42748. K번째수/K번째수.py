def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a=array[commands[i][0]-1:commands[i][1]]
        a.sort()
        answer.append(a[commands[i][2]-1]) #-1 안붙이면 6나와야하는거아닌가?(2번째 케이스)
    return answer