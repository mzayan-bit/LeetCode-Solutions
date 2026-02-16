class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        lenght = len(s)
        for i in range(lenght):
            seen=[]
            for j in range(i,lenght):
                if s[j] in seen:
                    break

                seen.append(s[j])
                longest = max(longest,len(seen))
        return longest


        