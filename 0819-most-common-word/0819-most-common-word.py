class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        banned = set(banned)
        d = {}
        p = paragraph.lower()
        for punct in "!?',;.":
            p = p.replace(punct, " ")
            
        for w in p.split():
            w = w.strip("#?")
            if w and w not in banned:
                d[w] = d.get(w, 0) + 1

        return max(d, key = d.get)