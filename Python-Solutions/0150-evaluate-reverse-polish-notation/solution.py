class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char not in "+-*/":
                stack.append(int(char))
            else:
                right = stack.pop()
                left = stack.pop()
                
                if char == "+":
                    stack.append(left + right)
                elif char == "-":
                    stack.append(left - right)
                elif char == "*":
                    stack.append(left * right)
                elif char == "/":
                    stack.append(int(left / right))
                    
        return stack[0]
