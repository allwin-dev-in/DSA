class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for n in nums:
            if n==0:
                rv=nums.remove(n)
                nums.append(0)
        print(nums)
        return

inst=Solution()
inst.moveZeroes(nums = [0,1,0,3,12])