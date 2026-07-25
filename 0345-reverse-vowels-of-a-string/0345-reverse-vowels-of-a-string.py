class Solution:
    def reverseVowels(self, s: str) -> str:
        m=""
        v="aeiouAEIOU"
        for i in s:
            if i in v:
                m+=i
        l,r,s,m=0,len(m)-1,list(s),list(m)
        while l<r:
            m[l],m[r]=m[r],m[l]
            l+=1
            r-=1
        j=0
        for i in range(len(s)):
            if s[i] in v:
                s[i]=m[j]
                j+=1
        
        s="".join(s)
        return s
