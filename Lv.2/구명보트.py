def solution(people, limit):
  people.sort()
  cnt = 0

  a = 0
  b = len(people) -1
  while a<b:
    if people[b]+people[a] <= limit:
      cnt += 1
      a += 1
    b -= 1
    return len(people) - cnt
