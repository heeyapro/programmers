def solution(brown,yellow):
  S = brown+yellow
  w = []
  h = []
  for i in range(1,S+1):
    if S%i == 0:
      w.append(i)
      h.append(i)
    for i in range(len(h)):
      if w[len(w)-1-i] >= h[i] or yellow == (w[len(w)-1-i]-2)*(h[i]-2):
        return [w[len(w)-1-i], h[i]]
