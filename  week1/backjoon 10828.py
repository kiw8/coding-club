import sys  # 입력 속도 향상을 위해 sys 모듈 사용

n = int(sys.stdin.readline())  # 첫 번째 줄: 명령어 개수 입력 받기

stack = []  # 스택을 저장할 리스트

for i in range(n):  # n번 반복하면서 명령어 처리
    command = sys.stdin.readline().split()  # 입력된 명령을 공백 기준으로 리스트로 변환

    if command[0] == 'push':  # push X: X를 스택에 추가
        stack.append(command[1])  # 스택의 끝에 요소 추가

    elif command[0] == 'pop':  # pop: 스택에서 마지막 요소 제거 및 출력
        if len(stack) == 0:  # 스택이 비어있다면 -1 출력
            print(-1)
        else:
            print(stack.pop())  # 스택의 마지막 요소 제거 및 출력 (LIFO)

    elif command[0] == 'size':  # size: 스택의 크기 출력
        print(len(stack))

    elif command[0] == 'empty':  # empty: 스택이 비어있는지 확인
        if len(stack) == 0:  # 비어있다면 1, 아니면 0 출력
            print(1)
        else:
            print(0)

    elif command[0] == 'top':  # top: 스택의 최상단(마지막) 요소 출력
        if len(stack) == 0:  # 스택이 비어있다면 -1 출력
            print(-1)
        else:
            print(stack[-1])  # 스택의 마지막 요소 출력