def solutuon(n):
  F = [0,1]
  for i in range(2,n+1):
    F.append(F[n-2]+F[n-1])
  if n>=2:
    F[n] = F[n]%1234567
  return F[n]
