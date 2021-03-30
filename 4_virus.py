import sys

# p, n을 공백으로 구분하여 입력받기
p, n = map(int, input().split())
# 매초 침입하는 바이러스의 수 입력받기
virus = list(map(int, input().split()))

temp = 0  # 연산값 저장을 위해 사용
result = 0

for i in range(n):
        temp += virus[i - 1] * p

# 최종 바이러스 개수를 1000000007로 나눈 나머지
result += temp % 1000000007

print(result)  # 최종 답안 출력