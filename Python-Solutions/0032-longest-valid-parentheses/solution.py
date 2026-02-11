class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1] # Base index to handle calculations from the start
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # If empty, this ')' is a mismatch; 
                    # use its index as the new starting boundary
                    stack.append(i)
                else:
                    # Current index minus the index of the last unmatched '('
                    max_len = max(max_len, i - stack[-1])
        
        return max_len
