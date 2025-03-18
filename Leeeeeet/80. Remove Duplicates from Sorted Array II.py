def removeDuplicates(nums):
        i=1
        for j in range(1,len(nums)):
            if i==1 or nums[j]!=nums[i-2]:
                nums[i]=nums[j]
                i+=1
        return i