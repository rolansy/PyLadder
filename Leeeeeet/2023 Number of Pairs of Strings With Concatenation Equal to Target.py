def numOfPairs( nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        s=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]+nums[j]==target:
                    s+=1
        return s
nums=["777","7","77","77"]
target="7777"
#4
print(numOfPairs(nums, target))
