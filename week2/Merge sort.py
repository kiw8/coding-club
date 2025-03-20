import sys  # 빠른 입출력을 위한 sys 모듈 사용

# 병합 정렬 함수 (Merge Sort)
def merge_sort(array):
    if len(array) <= 1:
        return array  # 원소가 1개 이하라면 그대로 반환 (정렬할 필요 없음)

    mid = len(array) // 2  # 배열을 반으로 나누는 중간 지점 설정
    left_half = merge_sort(array[:mid])  # 왼쪽 부분을 재귀적으로 정렬
    right_half = merge_sort(array[mid:])  # 오른쪽 부분을 재귀적으로 정렬

    return merge(left_half, right_half)  # 정렬된 두 부분을 병합하여 반환

# 정렬된 두 배열을 병합하는 함수
def merge(left, right):
    sorted_list = []  # 병합된 정렬된 리스트를 저장할 변수
    i, j = 0, 0  # 왼쪽, 오른쪽 배열을 비교할 인덱스 초기화

    # 두 리스트의 값을 비교하면서 작은 값을 sorted_list에 삽입
    while i < len(left) and j < len(right):
        if left[i] < right[j]:  # 왼쪽 배열의 값이 작으면 추가
            sorted_list.append(left[i])
            i += 1
        else:  # 오른쪽 배열의 값이 작으면 추가
            sorted_list.append(right[j])
            j += 1

    # 왼쪽 배열에 남아있는 요소들을 모두 추가
    sorted_list.extend(left[i:])
    # 오른쪽 배열에 남아있는 요소들을 모두 추가
    sorted_list.extend(right[j:])

    return sorted_list  # 병합된 정렬된 리스트 반환

# 빠른 입력 처리
N = int(sys.stdin.readline().strip())  # 첫 줄에서 입력받은 숫자 개수
array = [int(sys.stdin.readline().strip()) for _ in range(N)]  # N개의 정수를 입력받아 리스트로 저장

# 병합 정렬 실행 및 출력
sorted_array = merge_sort(array)  # 병합 정렬 실행

# 개선된 출력 방식 (가독성 ↑)
for num in sorted_array:
    print(num)  # 개행 출력
