class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3: return n

        pre1=3
        pre2=2
        cur=0

        for i in range(3,n):
            cur=pre1+pre2
            pre2=pre1
            pre1=cur
        
        return cur
        