class Solution:
    def findErrorNums(self, v: list[int]) -> list[int]:
        n=len(v)
        v.sort()
        m=[]
        for i in range(n-1):
            if v[i]==v[i+1]:
                m.append(v[i])
        for i in range(1,n+1):
            if i not in v:
                m.append(i)
                break
        return m