import sys

# k, p, n을 공백으로 구분하여 입력받기
k, p, n = map(int, input().split())

temp = 0  # 연산값 저장을 위해 사용
result = 0  # 최종 답안

temp += k

for i in range(n):
        temp *= p ** 10

# 최종 바이러스 개수를 1000000007로 나눈 나머지
result += temp % 1000000007

print(result)  # 최종 답안 출력