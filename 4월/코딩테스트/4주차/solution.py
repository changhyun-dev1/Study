# 모음사전
def solution(word):
    answer = 0
    dic = ['A', 'E', 'I', 'O', 'U']
    li = [5**i for i in range(len(dic))]
    
    for i in range(len(word)-1,-1,-1):
        idx = dic.index(word[i])
        for j in range(5-i):
            answer += li[j]*idx
        answer+=1
    return answer

# 구명보트
def solution(people, limit):
    answer=0
    people.sort()
    i=0;j=len(people)-1
    while i<=j:
        if people[i]+people[j] <= limit:
            i+=1;j-=1
            answer+=1
        else:
            j-=1
            answer+=1
    return answer

