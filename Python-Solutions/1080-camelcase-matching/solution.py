class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []    
        for query in queries:
            idx = 0  
            match = True
            for char in query:
                if idx < len(pattern) and char == pattern[idx]:
                    idx += 1
                elif char.isupper():
                    match = False
                    break
            res.append(match and idx == len(pattern)) 
        return res
