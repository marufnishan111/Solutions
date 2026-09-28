class Solution:
    def maxDepth(self, s: str) -> int:
        x,y=0,0
        m=[]
        for i in s:
            if i=='(':
                x+=1
            elif i==')':
                x-=1

            m.append(x)

        return max(m)