class Solution:
    def isMonotonic(self, n: List[int]) -> bool:
        x,y=1,1
        for i in range(len(n)-1):
            if n[i]<n[i+1]:
                x=0
                break
        for i in range(len(n)-1):
            if n[i]>n[i+1]:
                y=0
                break
        return x==1 or y==1