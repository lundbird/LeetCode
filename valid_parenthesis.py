def isValid(s):
    parens = {'(':')','{':'}','[':']'}
    stack = []
    for char in s:
        if char in parens:
            stack.append(char)
        else: 
            if not stack or parens[stack.pop()] != char:
                return False
    return not stack