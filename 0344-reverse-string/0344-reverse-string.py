class Solution:
    def reverseString(self, s: List[str]) -> None:
        # x=""
        # for i in s:
        #     x+=str(i)
        # s[:]=x[::-1]
        # return s

        l,r=0,len(s)-1
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        return s