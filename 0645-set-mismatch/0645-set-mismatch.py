class Solution:
    def findErrorNums(self, v: list[int]) -> list[int]:
        n=len(v)
        v.sort()
        m=0
        for i in range(n-1):
            if v[i]==v[i+1]:
                m=v[i]
                break
        s=(n*(n+1)//2)-sum(v)+m
        return [m,s]