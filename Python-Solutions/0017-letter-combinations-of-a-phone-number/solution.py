class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
            
        # Mapping as a dictionary or list
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        
        def solve(index, current_string):
            # Base case: if the string is the same length as digits, we're done
            if index == len(digits):
                res.append(current_string)
                return
            
            # Get the letters corresponding to the current digit
            letters = phone_map[digits[index]]
            
            # Loop through those letters
            for char in letters:
                # Recursive call: move to next digit and add current char
                solve(index + 1, current_string + char)
        
        solve(0, "")
        return res

# Example call:
# sol = Solution()
# print(sol.letterCombinations("23")) 
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
