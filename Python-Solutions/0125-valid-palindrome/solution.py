class Solution:
    def isPalindrome(self, s: str) -> bool:
        # new=''
        # for ch in s:
        #     if 97<=ord(ch)<=122:
        #         new+=ch
        #     elif 65<=ord(ch)<=90:
        #         new+=chr(ord(ch)+32)
        #     else:
        #         continue
        # return new==new[::-1] 
        new=''
        for ch in s:
            if ch.isalnum()==True:
                new+=ch.lower()
        return new[::-1]==new
