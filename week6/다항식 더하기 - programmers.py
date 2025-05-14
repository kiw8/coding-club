def solution(polynomial):
    poly_list = polynomial.split()

    x = 0  # x항의 계수를 저장할 변수
    s = 0  # 상수항의 합을 저장할 변수

    for p in poly_list:
        if p[-1] == 'x':
            if p[:-1]:
                x += int(p[:-1])
            else:
                x += 1
        elif p.isdigit():  # isdigit(): 우리가 필요한 '순수정수'만 확실하게 골라내는 것
            s += int(p)

    if x == 1:
        if s > 0:
            return f"x + {s}"
        else:
            return "x"
    elif x > 1:
        if s > 0:
            return f"{x}x + {s}"
        else:
            return f"{x}x"
    else:
        return f"{s}"


print(solution("3x + 7 + 2x + 6"))

