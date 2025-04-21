class Solution(object):
    def evalRPN(self, tokens):
        operators = ["+", "-", "*", "/"]
        stack = []
        
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                elif token == "/":
                    stack.append(int(float(a) / b))
        return int(stack.pop())