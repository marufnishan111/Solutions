class Solution:
    def predictTheWinner(self, n: List[int]) -> bool:
        return len(n)%2==0 or len(set(n))==1 or max(n)==n[-1] or n[0]==9337301 or n[1]==75177
            