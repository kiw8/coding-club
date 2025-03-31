import sys
input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용

# 상근이가 가지고 있는 카드 개수 입력
n = int(sys.stdin.readline())

# 상근이 카드 리스트 입력 받고 정렬
sangen = sorted(list(map(int, sys.stdin.readline().split())))  # 정렬은 이 코드에서 직접 쓰이진 않지만, 이진 탐색 등 다른 방식 대비용일 수 있음

# 찾고 싶은 카드 개수 입력
m = int(sys.stdin.readline())

# 찾고 싶은 카드 리스트 입력
cards = list(map(int, sys.stdin.readline().split()))

# 상근이 카드 개수를 세기 위한 딕셔너리 생성
dic1 = {}

# 상근이 카드 목록을 하나씩 돌면서 개수 세기
for x in sangen:
    if x in dic1:              # 이미 등장한 숫자라면
        dic1[x] += 1           # 기존 개수에 1을 더함
    else:                      # 처음 등장한 숫자라면
        dic1[x] = 1            # 개수를 1로 초기화
    print(dic1)
# 결과를 담을 리스트 생성
result = []

# 찾고자 하는 각 카드가 상근이 카드에 몇 개 있는지 확인
for y in cards:
    result.append(str(dic1.get(y, 0)))  # 있으면 개수, 없으면 0. 문자열로 변환해서 리스트에 추가
# 리스트를 공백으로 연결하여 한 줄로 출력
print(' '.join(result))