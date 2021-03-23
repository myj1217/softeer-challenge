n = int(input()) # n을 정수형으로 입력받는다

a = 2 # 연산을 위해 사용되는 변수
result = 0 # 결과값 출력을 위해 사용되는 변수

while True:
    if n == 0: # n이 0이라면 result를 연산하고 반복문 탈출
        result += a ** 2
        break
    a += a - 1
    n -= 1

print(result)