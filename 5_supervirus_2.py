import sys

# k, p, n을 공백으로 구분하여 입력받기
k, p, n = map(int, input().split())

result = 0

def virus(a, b):
        c = 0
        if b % 2 == 0:
                c += virus(a, b / 2)
                return c * c / 1000000007
        if b % 2 == 1:
                c += virus(a, b / 2)
                return c * c * a / 1000000007
        if b == 1:
                return a



# 최종 바이러스 개수를 1000000007로 나눈 나머지
result += k * virus(p, 10 * n)

print(result)  # 최종 답안 출력