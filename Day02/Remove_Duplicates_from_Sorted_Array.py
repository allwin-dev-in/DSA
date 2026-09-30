class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k=1
        for i in range(1,len(nums)):
            print(F"num[{i}]= {nums[i]}")
            print(F"num[{k-1}]= {nums[k-1]}")
            if nums[i]!=nums[k-1]:
                nums[k]=nums[i]
                k=k+1
        return k

ins=Solution()
print(ins.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))