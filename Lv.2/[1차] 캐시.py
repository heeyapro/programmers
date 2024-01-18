from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    memory = deque()
    for i in cities:
        i = i.lower()
        if (i in memory):
            answer += 1
            memory.remove(i)
            memory.append(i)
        else:
            answer += 5
            memory.append(i)
            if (len(memory) > cacheSize):
                memory.popleft()
            
    return answer
