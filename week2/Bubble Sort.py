def bubbleSort(arr):
    N = len(arr)  # 배열의 길이 (총 원소 개수)

    # 배열의 모든 요소를 순회하며 정렬 수행
    for i in range(N):
        # 현재 반복에서 마지막 i개의 요소는 이미 정렬된 상태이므로 비교할 필요 없음
        for j in range(N - 1 - i):
            # 인접한 두 원소를 비교하여 순서가 올바르지 않으면 교환 (swap)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 정렬할 배열 선언
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 버블 정렬 실행
bubbleSort(array)

# 정렬된 배열 출력
print(array)  # 출력 결과: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]