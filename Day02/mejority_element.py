class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        value = None
        count = 0 
        for num in nums:
            if count == 0:
                value = num
            if num == value:
                count += 1
            else:
                count-=1      
        return value

inst = Solution()
print(inst.majorityElement([2, 2, 1, 1, 1, 2, 2,3,4,5,6]))