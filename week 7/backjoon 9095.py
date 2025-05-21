import sys

n = int(input())   # 테스트 케이스 개수 입력

arr = [0] * 11     # dp 테이블, 0~10까지 총 11칸
arr[1] = 1         # 1을 만드는 방법: (1)
arr[2] = 2         # 2를 만드는 방법: (1+1), (2)
arr[3] = 4         # 3을 만드는 방법: (1+1+1), (1+2), (2+1), (3)

# 4부터 10까지의 값은 점화식 이용해서 계산
for i in range(4, 11):
    arr[i] = arr[i-1] + arr[i-2] + arr[i-3]

# 테스트 케이스 개수만큼 반복
for i in range(0, n):
    testNum = int(input())       # 정답을 구할 정수 n 입력 받기
    print(arr[testNum])          # DP 테이블에서 해당 n값의 정답 출력
