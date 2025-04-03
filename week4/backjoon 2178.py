from collections import deque  # BFS 구현을 위한 deque(덱) 라이브러리 사용

# ✅ BFS 함수 정의: (0, 0)에서 출발해서 (n-1, m-1)까지 최단거리 탐색
def bfs(x, y):
    queue = deque()             # 큐 생성
    queue.append((x, y))        # 시작점 좌표 (x, y)를 큐에 넣음

    while queue:                # 큐가 빌 때까지 반복
        x, y = queue.popleft()  # 큐에서 현재 위치 꺼냄

        # 현재 위치에서 상, 하, 좌, 우 방향으로 이동
        for i in range(4):
            nx = x + dx[i]      # 이동한 위치의 x좌표
            ny = y + dy[i]      # 이동한 위치의 y좌표

            # 이동한 위치가 미로 범위 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 이동한 위치가 벽(0)이라면 무시
            if graph[nx][ny] == 0:
                continue

            # 이동한 위치가 처음 방문하는 길(1)일 경우
            if graph[nx][ny] == 1:
                # 현재 위치의 값 + 1 을 저장 → 거리 증가
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))  # 다음 탐색을 위해 큐에 추가

    # 최종 목적지 (n-1, m-1)에 저장된 값이 최단거리
    return graph[n - 1][m - 1]

# ✅ 입력 받기: 첫 줄에 미로의 세로(n), 가로(m) 크기
n, m = map(int, input().split())

# ✅ 미로 정보 입력 받기
graph = []
for _ in range(n):
    # 입력 예시: "101111" → 각 문자를 숫자로 쪼개서 리스트로 변환
    row = list(map(int, list(input().strip())))
    graph.append(row)

# ✅ 방향 정의: 상, 하, 좌, 우 (dx, dy를 묶어서 4방향 이동 가능하게 함)
dx = [-1, 1, 0, 0]  # 위, 아래
dy = [0, 0, -1, 1]  # 왼쪽, 오른쪽

# ✅ BFS 수행 및 결과 출력
print(bfs(0, 0))  # 시작 좌표 (0, 0)에서 출발