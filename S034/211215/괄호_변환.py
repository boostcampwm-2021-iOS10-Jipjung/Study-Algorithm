def bracket_to_int(bracket):
    return 1 if bracket == "(" else -1

def int_to_bracket(_int):
    return "(" if _int == 1 else ")"

def split_to_balanced(w):
    if len(w) == 0:
        return "", ""
    u_count = bracket_to_int(w[0])
    i = 0
    for j in range(1, len(w)):
        i = j
        u_count += bracket_to_int(w[i])
        if u_count == 0:
            break
    return w[:i + 1], w[i + 1:]

def check_balanced_is_perfect(u):
    stack = []
    for char in u:
        if bracket_to_int(char) == 1:
            stack.append(1)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return True

# print(reverse_all_character("()"))
def reverse_all_character(u):
    result = ""
    for bracket in u:
        _int = bracket_to_int(bracket)
        reverse_bracket = int_to_bracket(-1 * _int)
        result += reverse_bracket
    return result

def solution(w):
    answer = ''
    if len(w) == 0:
        return answer
    
    u, v = split_to_balanced(w)
    if check_balanced_is_perfect(u):
        return u + solution(v)
    return "(" + solution(v) + ")" + reverse_all_character(u[1:-1])