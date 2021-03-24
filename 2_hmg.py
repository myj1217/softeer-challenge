import sys

name = sys.stdin.readline().rstrip() # 풀네임을 입력받는다

for i in name:
    if i.isupper(): # 글자가 대문자라면 출력
        print(i, end='')