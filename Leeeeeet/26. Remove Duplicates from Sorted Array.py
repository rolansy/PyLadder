def removeDuplicates(nums):
        i=1
        for j in range(1,len(nums)):
            if nums[j]!=nums[i-1]:
                nums[i]=nums[j]
                i+=1
        print(nums)
        return i
print(removeDuplicates([1,1,2])) # 2