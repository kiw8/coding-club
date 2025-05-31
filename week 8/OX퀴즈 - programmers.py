def solution(quiz):
    answer = []  # 최종 결과를 담을 리스트

    for q in quiz:
        # '='을 기준으로 수식과 정답으로 나누기
        exp, result = q.split('=')

        # eval() 함수: 문자열로 표현된 수식을 실제로 계산해서 결과값을 반환
        # exp_result: 문자열 수식의 실제 계산값을 저장하는 변수
        # 예: eval("3 + 2") -> 5
        exp_result = eval(exp)

        # 계산 결과와 문제의 정답 비교
        if exp_result == int(result):
            answer.append("O")  # 같으면 "O" 추가
        else:
            answer.append("X")  # 다르면 "X" 추가

    return answer  # 최종 결과 리스트 반환

if __name__ == "__main__":
    quiz_list = ["3 - 4 = -1", "5 + 2 = 6", "10 / 2 = 5", "7 * 3 = 21"]
    result = solution(quiz_list)
    print(result)
