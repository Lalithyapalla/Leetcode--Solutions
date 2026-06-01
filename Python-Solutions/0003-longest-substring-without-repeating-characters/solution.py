class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
     window = ""
     maxlen = 0
    
     for char in s:
        if char in window:
            window = window[window.index(char) + 1:]
        window += char
        maxlen = max(maxlen, len(window))
        
     return maxlen
    
