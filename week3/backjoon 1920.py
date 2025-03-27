# 이진 탐색 함수 (재귀 구현)
def search(array, target, start, end):
    # 찾는 값이 없는 경우 (탐색 범위가 유효하지 않음)
    if start > end:
        return None

    mid = (start + end) // 2  # 중간 인덱스 계산

    # 찾는 값을 발견한 경우
    if array[mid] == target:
        return mid
    # 찾는 값이 중간값보다 작으면 왼쪽 반 구간 재탐색
    elif array[mid] > target:
        return search(array, target, start, mid - 1)
    # 찾는 값이 중간값보다 크면 오른쪽 반 구간 재탐색
    else:
        return search(array, target, mid + 1, end)

# 입력 받을 숫자의 개수 (n)
n = int(input())

# n개의 정수를 입력받아 리스트 N에 저장
N = list(map(int, input().split()))
N.sort()  # 이진 탐색을 위해 오름차순 정렬

# 탐색할 숫자의 개수 (m)
m = int(input())

# m개의 정수를 입력받아 리스트 M에 저장
M = list(map(int, input().split()))

# M 리스트에 있는 숫자 각각에 대해 탐색 실행
for i in range(len(M)):
    target = M[i]  # 현재 탐색 대상
    result = search(N, target, 0, n - 1)  # 이진 탐색 실행

    # 결과에 따라 출력
    if result == None:
        print('0')  # 찾지 못한 경우
    else:
        print('1')  # 찾은 경우
