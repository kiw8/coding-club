from collections import deque

# DFS(깊이 우선 탐색) 함수 정의
def dfs(graph, v, visited):
    visited[v] = True  # 현재 노드를 방문 처리
    print(v, end=' ')  # 방문한 노드 출력

    # 인접 노드들을 오름차순으로 탐색
    for i in sorted(graph[v]):
        if not visited[i]:  # 방문하지 않은 노드라면 재귀적으로 방문
            dfs(graph, i, visited)

# BFS(너비 우선 탐색) 함수 정의
def bfs(graph, v, visited):
    queue = deque([v])  # 시작 노드를 큐에 삽입
    visited[v] = True  # 시작 노드를 방문 처리

    while queue:
        v = queue.popleft()  # 큐에서 노드를 꺼내 출력
        print(v, end=' ')

        # 현재 노드와 연결된 인접 노드들을 오름차순으로 확인
        for i in sorted(graph[v]):
            if not visited[i]:  # 방문하지 않은 노드를 큐에 삽입하고 방문 처리
                queue.append(i)
                visited[i] = True

# 정점의 개수(n), 간선의 개수(m), 시작 정점(k) 입력
n, m, k = map(int, input().split())

# 간선 정보를 저장할 리스트
edge_list = []
for _ in range(m):
    a, b = map(int, input().split())
    edge_list.append([a, b])

# 인접 리스트 방식으로 그래프 초기화 (노드 번호가 1번부터 시작하므로 n+1 크기로 생성)
graph = [[] for _ in range(n + 1)]

# 간선 정보를 바탕으로 양방향 연결 (무방향 그래프)
for a, b in edge_list:
    graph[a].append(b)
    graph[b].append(a)

# DFS와 BFS에서 사용할 방문 여부 리스트 (각 알고리즘마다 따로 사용)
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

# DFS 탐색 결과 출력
dfs(graph, k, visited_dfs)
print()  # 줄 바꿈

# BFS 탐색 결과 출력
bfs(graph, k, visited_bfs)
