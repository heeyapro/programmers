def solution(numbers):
    answer = []
    for i in numbers:
        if i % 2 == 0:
            answer.append(i+1)
        else:
            j = "0"+bin(i)[2:]
            idx = j.rfind("0")
            j = list(j)
            j[idx] ="1"
            j[idx+1] = "0"
            answer.append(int("".join(j),2))
    return answer
