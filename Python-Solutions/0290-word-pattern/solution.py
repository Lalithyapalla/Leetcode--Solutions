class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # ['a', 'b', 'b, 'c']
        #   |    |    |    |
        # [dog, cat, cat, dog]
        s_list = s.split()
        if len(pattern) != len(s_list):
            return False
        d = {}
        for i, j in zip(pattern, s_list):
            if i not in d:
                d[i] = j
            else:
                if d[i] != j:
                    return False
                else:
                    continue
        ss = set()
        for val in d:
            ss.add(d[val])
        return len(ss) == len(d)
