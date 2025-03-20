import sys  # 입력 속도 향상을 위해 sys 모듈 사용

n = int(sys.stdin.readline())  # 첫 번째 줄: 명령어 개수 입력 받기

deque = []  # 큐(Queue)를 저장할 리스트

for i in range(n):  # n번 반복하면서 명령어 처리
    command = sys.stdin.readline().split()  # 입력된 명령을 공백 기준으로 리스트로 변환

    if command[0] == 'push':  # push X: X를 큐에 추가
        deque.append(command[1])  # 큐의 끝(뒤)에 요소 추가

    elif command[0] == 'pop':  # pop: 큐에서 가장 앞의 요소 제거 및 출력
        if len(deque) == 0:  # 큐가 비어있다면 -1 출력
            print(-1)
        else:
            print(deque.pop(0))  # 큐의 가장 앞 요소 제거 및 출력 (FIFO)

    elif command[0] == 'size':  # size: 큐의 크기 출력
        print(len(deque))

    elif command[0] == 'empty':  # empty: 큐가 비어있는지 확인
        if len(deque) == 0:  # 비어있다면 1, 아니면 0 출력
            print(1)
        else:
            print(0)

    elif command[0] == 'front':  # front: 큐의 맨 앞 요소 출력
        if len(deque) == 0:  # 큐가 비어있다면 -1 출력
            print(-1)
        else:
            print(deque[0])  # 큐의 첫 번째 요소 출력

    elif command[0] == 'back':  # back: 큐의 맨 뒤 요소 출력
        if len(deque) == 0:  # 큐가 비어있다면 -1 출력
            print(-1)
        else:
            print(deque[-1])  # 큐의 마지막 요소 출력
