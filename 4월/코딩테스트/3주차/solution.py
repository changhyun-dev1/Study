# 마법의 엘리베이터

def solution(storey):
    answer = 0

    while storey:
        remainder = storey % 10
        if remainder > 5:
            answer += (10 - remainder)
            storey += 10
        elif remainder < 5:
            answer += remainder
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += remainder
        storey //= 10

    return answer

# 혼자서 하는 틱택토
