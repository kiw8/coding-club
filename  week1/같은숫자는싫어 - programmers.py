def solution(arr):
    answer = []  # 중복을 제거한 값을 저장할 리스트

    for i in range(len(arr)):  # 배열의 모든 요소를 순회
        if i == 0 or arr[i] != arr[i - 1]:
            # 첫 번째 원소는 무조건 추가 (i == 0)
            # 현재 원소(arr[i])가 이전 원소(arr[i - 1])와 다르면 추가
            answer.append(arr[i])

    print(answer)  # 결과를 출력
    return answer  # 최종적으로 정제된 리스트 반환

# 함수 실행 (중복 제거 테스트)
solution([1, 1, 2, 2, 5])
