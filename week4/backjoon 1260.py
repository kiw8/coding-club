from collections import deque

def dfs(graph, v, visited):
    visited[v] = True  # 방문 한 곳을 True로 변환
    print(v, end=' ')

    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, k = map(int, input().split())

edge_list = []
for _ in range(m):
    a, b = map(int, input().split())
    edge_list.append([a, b])

# 인접 리스트 초기화
graph = [[] for _ in range(n + 1)]

# 양방향 간선이므로 양쪽 다 추가
for a, b in edge_list:
    graph[a].append(b)
    graph[b].append(a)

visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)


dfs(graph, k, visited_dfs)
print()
bfs(graph, k, visited_bfs)

