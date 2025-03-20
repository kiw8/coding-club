array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]  # 정렬할 배열 선언

# 배열의 모든 원소를 순회하며 정렬 수행
for i in range(len(array)):  # i는 0부터 배열의 길이 -1까지 반복 (정렬이 진행될 인덱스)
    min_index = i  # 현재 위치를 기준으로 가장 작은 원소의 인덱스를 저장

    # 현재 위치(i) 이후의 요소들 중 최솟값을 찾음
    for j in range(i + 1, len(array)):  # i+1부터 배열의 끝까지 비교 수행
        if array[min_index] > array[j]:  # 현재까지 찾은 최소값보다 작은 값이 있으면
            min_index = j  # 최솟값의 인덱스를 업데이트

    # 찾은 최솟값과 현재 위치의 값을 교환 (스와프)
    array[i], array[min_index] = array[min_index], array[i]

# 정렬된 배열 출력
print(array)  # 출력 결과: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]