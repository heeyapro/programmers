def solution(s):
  S = list(s)
  stack = []
  
  for i in S:
    if stack and stack[-1] == i:
      stack.pop()
    else:
      stack.append()
      
  if len(stack) == 0:
    A = 1
  else:
    A = 0
    return A
      
