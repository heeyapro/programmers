from collections import Counter
def solution(clothes):
    answer = 1
    s = []
    for i in range(len(clothes)):
        s.append(clothes[i][1])
    c = sorted(Counter(s).values())

    for i in c:
        answer *= (i+1)
    answer -= 1
    return answer

#(카테고리 갯수 +1) * (카테고리 갯수 +1) -1
