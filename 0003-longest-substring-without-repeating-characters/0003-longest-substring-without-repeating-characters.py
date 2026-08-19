class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x=""
        m=0
        for i in s:
            if i in x:
                x=x[x.find(i)+1:]
            x+=i
            m=max(m,len(x))
        return m