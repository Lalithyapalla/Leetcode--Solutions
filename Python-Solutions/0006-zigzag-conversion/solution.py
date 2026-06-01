class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
                                
        r = [""] * numRows
        idx, d = 0, 1
        for c in s:
            r[idx] += c
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d      
                            
        return "".join(r)

