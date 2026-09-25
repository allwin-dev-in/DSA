class Solution:
    def maxSubArray(self, nums: list[int]):
        max_sum=float('-inf')
        cur_sum=0

        for i in nums:
            cur_sum += i
            max_sum=max(max_sum,cur_sum)
            if cur_sum<0:
                cur_sum =0

        return max_sum
  

inst=Solution()
print(inst.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))