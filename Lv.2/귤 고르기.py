from collections import Counter

def solution(k,tangerine):
  t = Counter(tangerine)
  s = sorted(t.values(), reverse=True)

  i = 0
  answer = 0
  while k > 0:
    k -= s[i]
    answer += 1
    i += 1
    if k == 0:
      break
    return answer
