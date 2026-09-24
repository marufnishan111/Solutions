class Solution:
    def smallestIndex(self, v: List[int]) -> int:
        n=len(v)
        for i in range(n):
            d=0
            s=str(v[i])
            for x in s:
                d+=(int(x))
            if d==i:
                return i
        return -1