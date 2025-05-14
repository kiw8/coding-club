# 입력 받기
n = int(input())                     # 사용자로부터 체스판의 크기 N을 입력받음

def n_queen(n):   # n_queen() 함수 정의
    count = 0                        # 배치 가능한 모든 퀸의 경우의 수를 저장할 변수
    board = [-1] * n                 # -1을 사용해서 아직 퀸이 아무 행에도 배치 되지 않았음을 표시 하기 위해


    # 행(row)과 열(col)에 퀸을 놓을 수 있는지 확인
    def is_safe(row, col):
        for prev in range(row):                          # 이전 행들(0 ~ row-1)을 확인

            if board[prev] == col:                          # board[prev]: 이전 행에 놓은 퀸의 열 번호
                return False

            if abs(board[prev] - col) == abs(prev - row):   # prev:이미 퀸을 놓은 행 번호 , 행차이=열차이:대각선 위에 있다는 뜻
                return False
        return True # 문제 없으면 안전한 위치

    def backtrack(row):
        nonlocal count  # 외부 변수 count 사용

        if row == n:  # 퀸 n개를 모두 놓았다면
            count += 1  # 경우의 수 1 증가
            return

        for col in range(n):  # 현재 행에서 가능한 모든 열 시도
            if is_safe(row, col):  # 해당 위치가 안전하면
                board[row] = col  # 퀸 배치
                backtrack(row + 1)  # 다음 행으로 이동
                board[row] = -1  # 배치 되돌리기 (백트래킹)

    backtrack(0)  # 0행부터 시작
    return count  # 가능한 모든 경우의 수 반환


print(n_queen(n))  # 정답 출력