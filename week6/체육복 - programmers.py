def solution(n, lost, reserve):
    # 여벌 체육복은 있지만 도난은 안 당한 학생 (진짜로 남에게 빌려줄 수 있는 학생)
    reserve_set = set(reserve) - set(lost)

    # 체육복을 도난당했지만 여벌은 없는 학생 (진짜로 빌려야 하는 학생)
    lost_set = set(lost) - set(reserve)

    # 여벌 있는 학생들이 도와줄 수 있는 앞뒤 번호 확인
    for r in reserve_set:
        # 앞 번호 학생이 체육복이 없으면 도와줌
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        # 앞 번호는 못 도와주고, 뒷 번호 학생이 체육복이 없으면 도와줌
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)

    # 전체 학생 수에서 체육복 못 받은 학생 수를 빼서 결과 리턴
    return n - len(lost_set)
