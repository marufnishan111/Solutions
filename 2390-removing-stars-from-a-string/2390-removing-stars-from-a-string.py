class Solution:
    def removeStars(self, s: str) -> str:
        x=""
        for i in s:
            x+=i
            if i=='*':
                x=x[:-2]
            
        return x