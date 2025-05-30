import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)  # 도달할 수 없는 최댓값

# 정점(V)과 간선(E)의 개수 입력
V, E = map(int, input().split())

# 시작 정점(K) 입력
K = int(input())

# 각 정점별로 연결된 간선 정보를 저장할 리스트
# graph[정점번호] = [(도착 정점, 가중치), ...]
graph = [[] for _ in range(V + 1)]

# 최단 거리 테이블: 모든 정점까지의 최단 거리값을 무한으로 초기화
distance = [INF] * (V + 1)

# 간선 정보 입력
for _ in range(E):
    u, v, w = map(int, input().split())
    # u에서 v로 가는 가중치 w인 간선 정보 저장
    graph[u].append((v, w))

def dijkstra(start):
    # 우선순위 큐(힙) 초기화
    q = []
    # 시작 정점까지의 비용은 0, (0, 시작정점) 형태로 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0  # 시작점의 최단거리는 0으로 설정

    while q:
        # 현재까지의 거리 dist, 현재 노드 now를 꺼냄
        dist, now = heapq.heappop(q)

        # 이미 더 짧은 최단거리가 갱신된 경우는 스킵
        if distance[now] < dist:
            continue

        # 현재 노드(now)와 연결된 인접 노드들 확인
        for v, w in graph[now]:
            cost = dist + w  # 현재 노드를 거쳐서 가는 비용 계산
            # 더 짧은 거리라면 최단 거리 테이블 갱신
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))  # 새로운 거리 정보를 우선순위 큐에 추가

# 다익스트라 알고리즘 실행
dijkstra(K)

# 모든 정점까지의 최단거리 출력
for i in range(1, V + 1):
    # 시작 정점에서 i까지 갈 수 없다면 INF 출력
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
