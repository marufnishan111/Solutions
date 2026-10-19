class Solution:
    def targetIndices(self, v: list[int], t: int) -> list[int]:
        n=len(v)
        v.sort()
        m=[]
        if t in v:
            x=v.index(t)
        
            while x<n and v[x]==t:
                m.append(x)
                x+=1
        return m