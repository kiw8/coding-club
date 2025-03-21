def solution(array, commands):
    answer = []  # 결과를 담을 리스트

    for i in range(len(commands)):  # 각 명령(command)을 하나씩 처리
        fill = []  # 자른 배열을 담을 임시 리스트

        # 현재 명령의 시작 인덱스(a)와 끝 인덱스(b)를 가져옴
        a = commands[i][0] - 1  # 인덱스는 0부터 시작하므로 -1
        b = commands[i][1]      # 자를 끝 인덱스 (슬라이싱은 b 전까지)

        # 구간의 원소들을 fill 리스트에 추가
        for _ in range(b - commands[i][0] + 1):
            fill.append(array[a])
            a = a + 1

        # 정렬
        sort = sorted(fill)

        # 정렬된 리스트에서 k번째 숫자를 결과에 추가
        answer.append(sort[commands[i][2] - 1])

    print(answer)
    return answer

'''
        array	                      commands	                 return               
[1, 5, 2, 6, 3, 7, 4]	 [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	    [5, 6, 3]

'''