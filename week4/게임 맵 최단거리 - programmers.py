from collections import deque  # BFS 구현을 위한 deque 라이브러리 사용

def solution(maps):
    n = len(maps)  # 맵의 세로 길이 (행)
    m = len(maps[0])  # 맵의 가로 길이 (열)

    # 상, 하, 좌, 우 방향 정의 (dx, dy 쌍으로)
    dx = [-1, 1, 0, 0]  # x축(열) 변화: 위, 아래
    dy = [0, 0, -1, 1]  # y축(행) 변화: 왼쪽, 오른쪽

    # BFS 탐색을 위한 큐 초기화 및 시작점 삽입
    queue = deque()
    queue.append((0, 0))  # 시작 위치는 좌측 상단 (0, 0)

    # 방문 여부를 저장할 2차원 리스트 초기화
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True  # 시작 위치는 방문 처리

    # BFS 시작
    while queue:
        x, y = queue.popleft()  # 현재 위치 꺼내기

        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]  # 새로운 x 좌표
            ny = y + dy[i]  # 새로운 y 좌표

            # 맵의 범위를 벗어난 경우는 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽(0)인 경우는 무시
            if maps[nx][ny] == 0:
                continue

            # 처음 방문하는 길(1)인 경우
            if not visited[nx][ny]:
                visited[nx][ny] = True  # 방문 처리
                # 현재 칸까지의 거리 + 1 저장
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))  # 큐에 다음 위치 추가

    # 도착 지점 (n-1, m-1)에 도달한 경우 거리 반환, 못했으면 -1 반환
    if visited[n - 1][m - 1]:
        return maps[n - 1][m - 1]
    else:
        return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))