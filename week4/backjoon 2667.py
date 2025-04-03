# 1은 집이 있는곳 0은 빈 공간을 뜻하며
# 상 하 좌 우로 연결된 1 끼리 하나의 단지로 가정하면
# 단지 수를 구하고 각 단지에서 포함된 집의 수를 오름차순으로 출력

# DFS를 사용 하여 1로 연결된 집들을 하나의 그룹(단지)로 묶기
# 지도를 한 칸씩 돌면서 1이면서 아직 방문 하지 않은 곳이 있을 시
# → 거기서 부터 DFS를 탐색을 시작함
# 다 끝나면 단지 하나 발견 완료 → 리스트 집 수 저장

# 지도의 크기 N 입력 (정사각형 지도)
n = int(input())

# N줄에 걸쳐 지도를 입력 받아 2차원 배열로 저장
# input().strip()은 줄 끝 개행 문자 제거, map(int, ...)으로 문자열 각 문자를 정수로 변환
graph = [list(map(int, input().strip())) for _ in range(n)]

# 방문 여부를 체크할 배열 (초기 값은 모두 False)
visited = [[False] * n for _ in range(n)]

# 상 하 좌 우 방향 벡터 (dx, dy는 방향을 의미함)
dx = [-1, 1, 0, 0]  # x좌표 이동: 위(-1), 아래(+1)
dy = [0, 0, -1, 1]  # y좌표 이동: 왼쪽(-1), 오른쪽(+1)

# DFS 함수 정의: (x, y)에서 시작 하여 연결된 집(1)을 탐색 하고, 단지 내 집 개수를 반환
def dfs(x, y):
    visited[x][y] = True  # 현재 위치를 방문 처리
    count = 1  # 현재 집 1개부터 시작

    # 상 하 좌 우 4방향 탐색(순회)
    for i in range(4):
        nx = x + dx[i]  # 새로 이동할 행
        ny = y + dy[i]  # 새로 이동할 열

        # 지도 범위를 벗어 나지 않고, 집이 있으며, 방문 하지 않았 다면 재귀적으로 DFS 호출
        if 0 <= nx < n and 0 <= ny < n: # 이 조건문은 2차원 배열(지도,행,열)의 범위를 벗어 나지 않도록 안전하게 탐색 하기 위해서 사용한 조건문
            if graph[nx][ny] == 1 and not visited[nx][ny]: # graph[nx][ny] == 1 이동한 위치에 집이 있는가? not visited[nx][ny] 그 집을 이미 탐색을 했는가?
                                                           # → 이미 탐색 된 집이면 다른 DFS 탐색 과정에서 단지로 포함되었음 (이 뜻은 중복 탐색을 방지해줌)
                count += dfs(nx, ny)  # 이어진 집 수를 누적

    return count  # 탐색이 끝난 단지 내 전체 집 수를 반환

# 각 단지에 속하는 집의 수를 저장할 리스트
result = []

# 전체 지도 순회
for i in range(n):
    for j in range(n):
        # 집이 있으며, 아직 방문 하지 않은 경우 → 새로운 단지 발견
        if graph[i][j] == 1 and not visited[i][j]:
            # graph[i][j] == 1이 이 좌표에 집이 존재 한건가?, not visited[i][j] 이 집을 이미 방문 해서 단지로 분류 했는가?
                                      # 이 구문은 만약 visited[i][j] == False 일때만, 즉 아직 방문하지 않은 집일 때만 탐색
            result.append(dfs(i, j))  # DFS 탐색 결과를 리스트에 추가

# 각 단지 내 집 수를 오름 차순 정렬
result.sort()

# 단지 수 출력
print(len(result))

# 각 단지 내 집 수 출력
for r in result:
    print(r)