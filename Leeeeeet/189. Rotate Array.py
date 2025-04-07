def rotate(nums, k):
        n=len(nums)
        p=(n-k)%n
        nums[:]=nums[p:]+nums[:p]