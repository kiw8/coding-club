import sys  # 빠른 입력을 위해 sys 모듈 사용

# 각 랜선을 주어진 길이(length)로 잘랐을 때 만들 수 있는 랜선 개수를 계산하는 함수
def get_count(lines, length):
    total = 0  # 총 개수 누적 변수
    for line in lines:
        # 해당 랜선을 length 길이로 잘랐을 때 몇 개 나오는지 계산
        total += line // length
    return total  # 누적된 개수 반환

# 전체 랜선 개수 K, 필요한 랜선 개수 N 입력 받기
K, N = map(int, sys.stdin.readline().split())

# K개의 랜선 길이를 한 줄씩 입력 받아 리스트로 저장
lines = [int(sys.stdin.readline()) for _ in range(K)]

# 이진 탐색 범위 설정
start = 1             # 랜선 최소 길이 (0으로 나누는 오류를 피하기 위해 1부터 시작)
end = max(lines)      # 가장 긴 랜선 길이까지 탐색
result = 0            # 만들 수 있는 최대 랜선 길이 결과값 저장 변수

# 이진 탐색 시작
while start <= end:
    mid = (start + end) // 2  # 현재 시도 중인 랜선 길이

    if mid == 0:
        # mid가 0이면 0으로 나누는 오류가 발생할 수 있으므로 반복 종료
        break

    mid_count = get_count(lines, mid)  # mid 길이로 잘랐을 때 만들 수 있는 랜선 개수

    if mid_count < N:
        # 원하는 개수보다 적게 만들면 더 짧게 잘라야 하므로 왼쪽 구간 탐색
        end = mid - 1
    else:
        # 원하는 개수 이상 만들 수 있다면, 일단 저장하고 더 긴 길이도 시도해봄
        result = mid
        start = mid + 1

# 최종적으로 가능한 최대 랜선 길이를 출력
print(result)
