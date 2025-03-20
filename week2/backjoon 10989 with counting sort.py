import sys
input = sys.stdin.readline
output = sys.stdout.write  # 🔹 sys.stdout.write()를 변수에 저장하여 최적화

# 🔹 [1] 입력 개수 받기
n = int(input())

# 🔹 [2] 계수 정렬을 위한 배열 선언 (숫자의 범위: 1 ~ 10,000)
count = [0] * 10001

# 🔹 [3] 숫자의 개수를 기록 (입력 최적화)
for _ in range(n):
    count[int(input())] += 1

# 🔹 [4] 등장한 숫자를 한 줄씩 출력 (출력 최적화)
for i in range(10001):
    if count[i] > 0:
        output(f"{i}\n" * count[i])  # 등장 횟수만큼 한 번에 출력 (메모리 절약 & 속도 향상)
