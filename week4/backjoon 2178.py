from collections import deque

# BFS 함수 정의
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]

# ✅ 입력 받기 (수정됨!)
n, m = map(int, input().split())

# 그래프 정보 입력 받기
graph = []
for _ in range(n):
    graph.append(list(map(int, list(input().strip()))))

# 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 결과 출력
print(bfs(0, 0))
