class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        print(s)
   
        

inst=Solution()
inst.reverseString(["h","e","l","l","o"])