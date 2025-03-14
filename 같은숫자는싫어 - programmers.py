def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i - 1]:
            answer.append(arr[i])
    print(answer)
    return answer

solution([1, 1, 2, 2, 5])