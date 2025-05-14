n, m = map(int, input().split())  # 1~n 중에서 중복 없이 m개 고르기
used = [False] * (n + 1)  # 숫자 사용 여부 체크 (1-based index)
result = []  # 현재 순열을 저장할 리스트


def back():
    if len(result) == m:  # m개를 모두 골랐다면
        print(*result)  # 공백 구분으로 출력 (예: 1 2 3)
        return

    for i in range(1, n + 1):  # 1부터 n까지 숫자 시도
        if not used[i]:  # 아직 사용하지 않은 숫자라면
            used[i] = True  # 사용 표시
            result.append(i)  # 숫자 추가
            back()  # 다음 숫자 고르러 재귀 호출
            result.pop()  # 마지막 숫자 제거 (되돌리기)
            used[i] = False  # 사용 취소 (다른 경우를 위해)


back()  # 순열 생성 시작

