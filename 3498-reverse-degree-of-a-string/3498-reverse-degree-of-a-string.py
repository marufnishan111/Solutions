class Solution:
    def reverseDegree(self, s: str) -> int:
        m,x=0,1
        for i in s:
           m+=((123-ord(i))*x)
           x+=1
        return m