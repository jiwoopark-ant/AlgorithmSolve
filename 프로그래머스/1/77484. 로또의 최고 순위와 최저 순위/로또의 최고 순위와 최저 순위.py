# def solution(lottos, win_nums):
#     ranking=6
#     for i in lottos:
#         if i in win_nums:
#             ranking-=1
#     a=lottos.count(0)-1
#     print(a)
#     answer = [ranking-a,ranking+a]
#     return answer

def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1] 
    cnt_0 = lottos.count(0) 
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]