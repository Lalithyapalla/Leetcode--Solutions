class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res=[]
        for word in words:  
            n=''
            for ch in word:
                if ch in 'qwertyuiopQWERTYUIOP':
                    n+='1'
                elif ch in 'asdfghjklASDFGHJKL':
                    n+='2'
                elif ch in 'zxcvbnmZXCVBNM':
                    n+='3'
            if len(n)==2:
                if n[0]==n[1]:
                    res+=[word]
            elif len(set(n))==1:
                res+=[word]
                
        return res
