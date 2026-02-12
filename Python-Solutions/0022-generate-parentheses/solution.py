class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
    
        def backtrack(s, left, right):
            # Base case: the string is full
            if len(s) == 2 * n:
                res.append(s)
                return
            
            # If we have open brackets left to use, add '('
            if left < n:
                backtrack(s + "(", left + 1, right)
                
            # Only add ')' if it won't "break" the math (right < left)
            if right < left:
                backtrack(s + ")", left, right + 1)
                
        backtrack("", 0, 0)
        return res
