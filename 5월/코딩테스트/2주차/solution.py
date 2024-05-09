# 단속카메라
def solution(routes):
    routes.sort() 
    answer = 1 
    start, end = routes[0][0], routes[0][1]
    for i in routes[1:]:
        if start <= i[0] <= end:
            start = i[0] 
            end = min(end, i[1])
        else:
            start, end = i[0], i[1]
            answer += 1 
    return answer

# 연속된 부분 수열의 합
def solution(sequence, k):
    l = r = 0
    answer = [0, len(sequence)]
    sum = sequence[0]

    while True:
        if sum < k:
            r += 1
            if r == len(sequence): break
            sum += sequence[r]
        else:
            if sum == k:
                if r-l < answer[1]-answer[0]:
                    answer = [l, r]
            sum -= sequence[l]
            l += 1
    return answer

