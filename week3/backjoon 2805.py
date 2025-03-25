def get_count(trees, height):
    """현재 절단기 높이로 자를 때 얻을 수 있는 나무의 총 길이를 계산하는 함수"""
    total = 0
    for tree in trees:
        if tree > height:
            total += tree - height  # 자른 부분만 누적
    return total


N, M = map(int, input().split())  # N: 나무의 수, M: 가져가야 할 나무 길이
trees = list(map(int, input().split()))  # 각 나무의 높이 리스트

start = 0                  # 절단기 높이의 최소값 (0부터 시작 가능)
end = max(trees)           # 절단기 높이의 최대값 (가장 큰 나무 높이까지 가능)
result = 0                 # M미터 이상을 얻을 수 있는 절단기 높이 중 가장 큰 값 저장

while start <= end:
    mid = (start + end) // 2  # 현재 탐색 중인 절단기 높이 (이진 탐색의 중앙값)

    mid_count = get_count(trees, mid)  # 현재 절단기 높이(mid)로 자를 때 얻는 나무의 총 길이

    if mid_count < M:
        # 자른 나무 길이가 부족하면 절단기 높이를 낮춰야 함 (더 많이 잘라야 하니까)
        end = mid - 1
    else:
        # 자른 나무 길이가 충분하면 일단 이 높이를 저장하고
        result = mid
        # 더 높은 절단기로도 가능한지 탐색해본다 (더 아끼기 위해)
        start = mid + 1

# 최종적으로 저장된 result가 조건을 만족하는 가장 높은 절단기 높이
print(result)
