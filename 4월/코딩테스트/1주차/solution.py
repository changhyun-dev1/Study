# 의상
def solution(clothes):
    hash_map = {}
    for clothe, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1
        
    answer = 1
    for type in hash_map:   
        answer *= (hash_map[type] + 1)
    
    return answer - 1

print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))

# 피로도
from itertools import permutations

def solution(k, dungeons):
    answer = 0

    all = list()
    for i in permutations(dungeons, len(dungeons)):
        all.append(i)
    
    count = list()
    for i in all:
        power = k
        cnt = 0
        for j in i:
            if (j[0] <= power):
                power -= j[1]
                cnt += 1

        count.append(cnt)

    answer = max(count)
    return answer
