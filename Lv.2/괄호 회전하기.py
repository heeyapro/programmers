def solution(s):
    cnt = 0

    for i in range(len(s)):
        stack = []
        for j in s:
            if not stack:
                stack.append(j)
                continue
            if stack[-1] == "[" and j == "]":
                stack.pop()
            elif stack[-1] == "{" and j == "}":
                stack.pop()
            elif stack[-1] == "(" and j == ")":
                stack.pop()
            else:
                stack.append(j)
        s = s[1:] + s[0]
        if not stack:
            cnt += 1
    return cnt
