class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in list(nums):
            if i== val:
                nums.remove(i)
        return len(nums)

inst=Solution()
inst.removeElement([0,1,2,2,3,0,4,2],val=2)