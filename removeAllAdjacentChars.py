def removeDuplicates(self, S: str) -> str:
    stack = [""]
    for c in S:
        stack.pop() if stack[-1]==c else stack.append(c)
    return ''.join(stack)