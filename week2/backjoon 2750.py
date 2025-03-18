import sys  # sys 모듈을 가져와 빠른 입력을 처리할 수 있도록 함

# 첫 번째 줄에서 정수 N을 입력받음 (정렬할 숫자의 개수)
n = int(sys.stdin.readline().strip())

# N개의 정수를 입력받아 리스트(array)에 저장 (리스트 컴프리헨션 사용)
array = [int(sys.stdin.readline().strip()) for _ in range(n)]

# 선택 정렬 알고리즘 시작
for i in range(len(array)):  # 리스트의 길이만큼 반복 (0부터 len(array)-1까지)
    min_index = i  # 현재 위치를 기준으로 가장 작은 값의 인덱스를 저장

    # i번째 원소 이후의 값들과 비교하여 최솟값 찾기
    for j in range(i + 1, len(array)):  # i+1부터 리스트 끝까지 반복
        if array[min_index] > array[j]:  # 현재까지 찾은 최솟값보다 더 작은 값이 있다면
            min_index = j  # 최솟값의 인덱스를 업데이트

    # 찾은 최솟값과 현재 위치의 값을 교환 (스와프)
    array[i], array[min_index] = array[min_index], array[i]

# 정렬된 결과를 한 줄씩 출력
for num in array:  # 리스트의 모든 요소를 하나씩 가져와 출력
    print(num)  # 한 줄씩 출력