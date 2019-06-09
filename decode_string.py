class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for c in s:
            if c == "]":
                cur_word = []
                cur_char = stack.pop()
                while cur_char != "[":
                    cur_word.append(cur_char)
                    cur_char = stack.pop()
                
                repeat_count = int(stack.pop())    
                stack.extend((cur_word[::-1])*repeat_count)
            else:
                stack.append(c)
        return ''.join(stack)