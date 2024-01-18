def solution(order):
    p_stack = []
    c_box = 1
    l_box = 0  

    for i in order:
        while c_box <= i:
            p_stack.append(c_box)
            c_box += 1

        if p_stack and p_stack[-1] == i:
            p_stack.pop()
            l_box += 1
        else:
            break

    return l_box
