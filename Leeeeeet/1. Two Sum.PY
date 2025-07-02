from typing import List

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a=nums[i]
            b=(target-a)
            if b in nums[i+1:]:
                return [i,nums[i+1:].index(b)+1+i]
        return []
    
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={}

        for i,n in enumerate(nums):
            diff=target-n
            if diff in prevMap:
                return [i,prevMap[diff]]
            prevMap[n]=i