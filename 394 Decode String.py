class Solution:
    def decodeString(self, s: str) -> str:
        word_stack = []
        n = len(s)
        for i in range(n):
            if s[i] != "]":
                word_stack.append(s[i])
            else:
                word = ""
                while word_stack[-1] != "[":
                    word = word_stack.pop() + word
                # pop "["
                word_stack.pop()
                num = ""
                while word_stack and word_stack[-1].isdigit():
                    num = word_stack.pop() + num
                
                word_stack.append(word * int(num))
        
        return "".join(word_stack)