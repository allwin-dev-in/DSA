class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted([x**2 for x in nums])
    

inst=Solution()
inst.sortedSquares([-4,-1,0,3,10])