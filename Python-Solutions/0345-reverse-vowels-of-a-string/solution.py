class Solution:
    def reverseVowels(self, s: str) -> str:
        d = []   
        idx = []  
        list1 = list(s) 
        for i in range(len(s)):
            if (s[i] in 'aeiou' ) or (s[i] in 'AEIOU'):
                d.append((s[i]))
                idx.append(i)
        for ele ,i in zip(d[::-1],idx):
             list1[i] = ele
             
        return "".join(list1)
