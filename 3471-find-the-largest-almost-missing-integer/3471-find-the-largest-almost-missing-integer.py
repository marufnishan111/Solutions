class Solution:
    def largestInteger(self, n: List[int], k: int) -> int:
        if k==len(n):
            return max(n)
        if k==1:
            n.sort(reverse=True)
            
            for i in n:
                if n.count(i)==1:
                    return i

        x,y=n[0],n[-1]
        a,b=n.count(x),n.count(y)
        if a==1 and b==1:
            return max(x,y)
        elif a==1:
            return x
        elif b==1:
            return y
        else:
            return -1