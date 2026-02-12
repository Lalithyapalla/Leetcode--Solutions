class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        num = 0
        sign = 1 # 1 is positive, -1 is negative
        for char in s:
            if char.isdigit():
                # Build the number (handles multi-digit like '123')
                num = num * 10 + int(char)
            elif char == '+':
                res += sign * num
                num = 0
                sign = 1
            elif char == '-':
                res += sign * num
                num = 0
                sign = -1
            elif char == '(':
                # Save the current result and sign to the stack
                stack.append(res)
                stack.append(sign)
                # Reset for the new expression inside brackets
                res = 0
                sign = 1
            elif char == ')':
                res += sign * num
                num = 0
                # Pop the sign first, then the previous result
                res *= stack.pop() # This is the sign before '('
                res += stack.pop() # This is the result before '('
                
        return res + (sign * num)
