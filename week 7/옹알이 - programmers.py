def solution(babbling):
    answer = 0
    for bab in babbling:
        # 발음 가능한 단어들을 숫자 "0"으로 치환
        bab = bab.replace("aya", "0")
        bab = bab.replace("ye", "0")
        bab = bab.replace("woo", "0")
        bab = bab.replace("ma", "0")

        # 치환 결과가 모두 숫자일 경우 (= 허용된 단어만 포함되었을 경우)
        if bab.isdigit():
            answer += 1

    return answer  # 조건을 만족하는 단어의 개수 반환