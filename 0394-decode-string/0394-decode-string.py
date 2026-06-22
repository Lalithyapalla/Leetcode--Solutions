class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ''
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                stack.append((cur_str, num))
                cur_str = ''
                num = 0
            elif char == ']':
                prev, now = stack.pop()
                cur_str = prev + (now * cur_str)
            else:
                cur_str += char
        return cur_str
