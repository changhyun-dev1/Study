import heapq

def solution(n, works):
    answer = 0

    if (sum(works) <= n):
        answer = 0
    else:
        works = [-i for i in works]
        heapq.heapify(works)
        
        while (n > 0):
            heapq.heappush(works, heapq.heappop(works) + 1)
            n -= 1
        
        for i in works:
            answer += i ** 2
        
    return answer


# works 배열 내 모든 원소들의 제곱값의 합을 최소로 만드는 것
# 1. heap 자료구조를 사용하기 위해 heapq 모듈을 불러온다. import heapq
# 2. 만약 작업의 총량이 남은 시간 안에 다 할 수 있으면 if (sum(works) <= n)
# 3. 피로도는 없다. answer = 0
# 4. 반면에 작업을 남은 시간 안에 다 할 수 없다면 else
# 5. 최대 힙 정렬을 위해 작업 시간을 음수로 바꾸어 리스트를 새로 저장한다. works = [-i for i in works]
# 6. 새로 저장한 리스트를 heap 자료구조로 바꾼다. heapq.heapify(works)
# 7. 퇴근할 때까지 반복하며 while (n > 0)
# 8. 최대 힙에서 최댓값을 추출하고 그 값에 1을 더한 뒤(가장 많이 남은 작업을 1시간 수행), 해당 값을 최대 힙에 추가한다. heapq.heappush(works, heapq.heappop(works) + 1)
# 9. 1시간 동안 작업을 수행하였으므로 남은 퇴근 시간을 1시간 줄인다. n -= 1
# 10. 퇴근시간이 다 되었으면 남은 작업의 양을 하나씩 추출하여 야근 지수를 계산한다. for i in works: answer += i ** 2 
