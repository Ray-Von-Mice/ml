class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        num_stack = []
        result = 0
        for token in tokens:
            if token == "+":
                result = num_stack.pop() + num_stack.pop()
                num_stack.append(int(result))
            elif token == '-':
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                result = num2 - num1
                num_stack.append(int(result))
            elif token == '*':
                result = num_stack.pop() * num_stack.pop()
                num_stack.append(int(result))
            elif token == '/':
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                result =  num2 / num1
                num_stack.append(int(result))
            else:
                num_stack.append(int(token))
        return num_stack[0]
