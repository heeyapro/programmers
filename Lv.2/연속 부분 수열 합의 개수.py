def solution(elements):
  l = len(elements)
  e = elements*2
  s = set()

  for i in range(l):
    for j in range(l):
      s.add(sum(e[j:j+i+1]))

  return len(s)
