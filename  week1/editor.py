import sys  # 빠른 입력을 위해 sys 모듈 사용

# 초기 문자열 입력 -> 리스트로 변환하여 왼쪽 스택(l_stack)에 저장
l_stack = list(sys.stdin.readline().strip())  # strip()을 사용해 개행문자 제거
r_stack = []  # 커서 오른쪽의 문자들을 저장할 스택

# 명령어 개수 입력
n = int(sys.stdin.readline().strip())  # 개행문자 제거 후 정수 변환

# n번의 명령어 입력 및 실행
for _ in range(n):
    command = sys.stdin.readline().split()  # 공백 기준으로 명령어와 인수 분리

    # 1️⃣ 커서를 왼쪽으로 이동 (L)
    if command[0] == 'L':
        if len(l_stack) >= 1:  # 왼쪽 스택이 비어있지 않다면 (커서가 맨 앞이 아닐 때)
            r_stack.append(l_stack.pop())  # 왼쪽 스택에서 pop()한 문자를 오른쪽 스택으로 이동

    # 2️⃣ 커서를 오른쪽으로 이동 (D)
    elif command[0] == 'D':
        if len(r_stack) >= 1:  # 오른쪽 스택이 비어있지 않다면 (커서가 맨 뒤가 아닐 때)
            l_stack.append(r_stack.pop())  # 오른쪽 스택에서 pop()한 문자를 왼쪽 스택으로 이동

    # 3️⃣ 커서 왼쪽의 문자 삭제 (B)
    elif command[0] == 'B':
        if len(l_stack) >= 1:  # 왼쪽 스택이 비어있지 않다면 (삭제할 문자가 있을 때)
            l_stack.pop()  # 왼쪽 스택에서 pop()하여 삭제

    # 4️⃣ 커서 왼쪽에 새로운 문자 추가 (P $)
    elif command[0] == 'P':
        l_stack.append(command[1])  # 입력받은 문자(command[1])를 왼쪽 스택에 추가

# 🔹 커서 오른쪽(r_stack)에 있는 문자를 뒤집어서 왼쪽 스택(l_stack)에 붙이기
l_stack.extend(reversed(r_stack))  # r_stack은 스택 구조이므로, reversed() 사용하여 원래 순서대로 합침

# 🔹 리스트(l_stack)를 문자열로 변환하여 최종 출력
print(''.join(l_stack))  # 리스트의 문자들을 이어 붙여 출력
