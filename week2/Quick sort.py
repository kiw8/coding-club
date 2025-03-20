array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]  # 정렬할 배열


def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개 이하이면 정렬할 필요 없음
        return

    pivot = start  # 피벗을 첫 번째 원소로 설정
    left = start + 1  # 왼쪽 포인터 (피벗 다음 위치)
    right = end  # 오른쪽 포인터 (배열 끝 위치)

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:  # 엇갈린 경우 (작은 값과 피벗 교체)
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 작은 값과 큰 값을 교체
            array[left], array[right] = array[right], array[left]

    # 분할 후, 왼쪽과 오른쪽을 각각 정렬
    quick_sort(array, start, right - 1)  # 왼쪽 부분 정렬
    quick_sort(array, right + 1, end)  # 오른쪽 부분 정렬


quick_sort(array, 0, len(array) - 1)

print(array)  # 정렬 결과 출력