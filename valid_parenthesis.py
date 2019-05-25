def isValid(s):
    parens = {'(':')','{':'}','[':']'}
    stack = []
    for char in s:
        if char in parens:
            stack.append(char)
        else: #no other character types so else works
            if not stack or parens[stack.pop()] != char:
                return False
    return False if stack else True