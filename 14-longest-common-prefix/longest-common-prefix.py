class Solution:
    def longestCommonPrefix(self, s: list[str]) -> str:
        if not s: return ""
        s.sort()
        f, l, p = s[0], s[-1], ""
        for i in range(min(len(f), len(l))):
            if f[i] != l[i]:
                break
            p += f[i]
            
        return p