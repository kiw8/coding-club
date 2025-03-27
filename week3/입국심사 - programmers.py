def solution(n, times):
    # 가능한 심사 시간의 범위를 설정
    # 최소 시간은 1분, 최대 시간은 가장 느린 심사관이 n명을 모두 심사할 경우
    start, end = 1, max(times) * n

    # 이진 탐색을 통해 최소 시간을 찾아나감
    while start <= end:
        mid = (start + end) // 2  # 현재 시간 후보 (중간값)
        people = 0  # 총 인원 누적 변수

        # 각 심사관이 mid 시간 동안 몇 명을 심사할 수 있는지 계산
        for i in times:
            people += mid // i  # mid 시간 동안 i초 걸리는 심사관이 처리할 수 있는 사람 수

        # 심사 가능한 사람이 부족하다면 → 시간이 더 필요하다 → 오른쪽으로 탐색
        if people < n:
            start = mid + 1

        # 심사 가능한 사람이 충분하거나 많다면 → 시간이 남을 수 있다 → 왼쪽으로 탐색
        else:
            end = mid - 1

    # start는 모든 사람을 심사할 수 있는 최소 시간으로 수렴됨
    return start
