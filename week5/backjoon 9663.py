# 사용자로부터 체스판의 크기 n 입력받음
n = int(input())  # 예: 4

def n_queen(n):
    count = 0  # 가능한 퀸 배치 경우의 수 저장
    board = [-1] * n  # board[i] = i행의 퀸이 있는 열 번호, 초기에는 -1로 모두 미배치 상태

    # (row, col)에 퀸을 놓을 수 있는지 확인하는 함수
    def is_safe(row, col):
        for prev in range(row):  # 현재 행은 아직 놓기 전이므로 이전 행들(0 ~ row-1)만 검사
            if board[prev] == col:
                return False  # 같은 열에 퀸이 이미 있음
            if abs(board[prev] - col) == abs(prev - row):
                return False  # 대각선상에 충돌
        return True

    # 백트래킹 함수: row행에 퀸을 배치하는 함수
    def backtrack(row):
        nonlocal count

        # row == n이면 퀸을 모두 배치한 상태 → 유효한 경우
        if row == n:
            # board 상태 예: [1, 3, 0, 2] → 아래와 같은 체스판
            # . Q . .
            # . . . Q
            # Q . . .
            # . . Q .
            count += 1
            return

        # 현재 행(row)에 대해 가능한 모든 열(col)을 시도
        for col in range(n):
            if is_safe(row, col):  # 해당 위치가 안전하다면
                board[row] = col  # 퀸을 배치

                # 디버깅 출력: 현재 row와 board 상태 출력 (원하면 주석 해제)
                # print(f"row={row}, board={board}")

                backtrack(row + 1)  # 다음 행으로 이동 (재귀)

                board[row] = -1  # 백트래킹: 퀸 배치를 되돌림

    backtrack(0)  # 0행부터 시작
    return count  # 가능한 경우의 수 반환

# 결과 출력
print(n_queen(n))
