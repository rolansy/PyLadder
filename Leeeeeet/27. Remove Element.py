class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        while val in nums:
            nums.remove(val)
            n-=1
        return n