def solution(s):
  s = s.split(" ")
  for i in range(len(s)):
    s[i] = s[i].capitalize()
  v = " ".join(s)
  return v
