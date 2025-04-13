n, m = map(int, input().split())
used = [False] * (n + 1)
result = []

def back():
    if len(result) == m:
        print(*result)   # 언패킹 연산자 예를 들어 [1, 2, 3, 4]면
        return           # 출력할 때 [1, 2, 3, 4]가 아닌
                         # 1 2 3 4 를 출력
    for i in range(1, n + 1):
        if not used[i]:
            used[i] = True
            result.append(i)
            back()       # 맨 위의 if문에서 return하면 여기로 돌아옴.
            result.pop()
            used[i] = False

back()

