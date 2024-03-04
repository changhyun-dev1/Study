def solution(denum1, num1, denum2, num2):
    answer = []
    num = denum1*num2 + denum2*num1 # 분자
    deno = num2*num1                # 분모

    gcd = 0
    # num과 deno의 최대공약수 구하기
    for j in range(min(num,deno), 0, -1):
        if num % j == 0 and deno % j ==0:
            gcd = j
            break

    answer = [num//gcd, deno//gcd]
    return answer
