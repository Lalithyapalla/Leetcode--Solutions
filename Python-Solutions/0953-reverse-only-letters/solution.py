class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = []
        m = []
        
        for i in range(len(s)):
            if not s[i].isalpha():
                l.append((i, s[i])) 
            else:
                m.append(s[i])
        
        m = m[::-1]
        for index, char in l:
            m.insert(index, char)
            
        return "".join(m)
