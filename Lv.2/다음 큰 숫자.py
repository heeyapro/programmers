def solution(n):
  answer = 0
  m = n
  n_b = bin(n)[2:]
  while True:
    m += 1
    m_b = bin(m)[2:]
    if n_b.count("1") == m_b.count("1"):
      answer = m
      break
  return answer
