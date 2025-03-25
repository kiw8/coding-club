def binary_search(array, target):
    # 시작 인덱스와 끝 인덱스를 설정
    start = 0
    end = len(array) - 1

    # 시작 인덱스가 끝 인덱스보다 작거나 같을 때까지 반복
    while start <= end:
        # 중간 인덱스를 계산
        mid = (start + end) // 2

        # 중간 값이 찾고자 하는 값과 같으면 인덱스를 반환
        if array[mid] == target:
            return mid

        # 중간 값이 타겟보다 크면 왼쪽 부분 탐색
        elif array[mid] > target:
            end = mid - 1

        # 중간 값이 타겟보다 작으면 오른쪽 부분 탐색
        else:
            start = mid + 1

    # 반복문이 끝날 때까지 찾지 못하면 None 반환
    return None
