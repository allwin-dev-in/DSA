class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in nums:
            if nums.count(i) >1:
                return True 
        else:
            return False

inst=Solution()
print(inst.containsDuplicate([2,14,18,22,22]))
