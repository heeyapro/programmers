def solution(n):
  F = [1,1]
  for i in range(2,n+1):
    F.append([i-2]+[i-1])
  if n>=2:
    F[n] = F[n]%1234567
  return F[n]
