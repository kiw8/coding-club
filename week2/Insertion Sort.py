array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]  # 정렬할 배열 선언

# 두 번째 원소(index 1)부터 마지막 원소까지 반복하며 정렬 수행
for i in range(1, len(array)):
    # 현재 선택한 원소를 정렬된 부분과 비교하며 적절한 위치에 삽입
    for j in range(i, 0, -1):  # j는 i부터 1까지 감소하면서 반복 (왼쪽 방향으로 비교)
        if array[j] < array[j - 1]:  # 현재 값이 왼쪽 값보다 작으면 위치 변경 (swap)
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            # 자기보다 작은 데이터를 만나면 해당 위치에서 정렬이 완료되므로 중단
            break

# 정렬된 배열 출력
print(array)  # 출력 결과: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]