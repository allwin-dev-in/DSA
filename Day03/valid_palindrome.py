class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= "".join(i.lower() for i in s if i.isalpha()or i.isnumeric())
        print(s)
        rev_s= s[::-1]
        print(rev_s)
        if s==rev_s:
            return True
        else:
            return False


inst=Solution()
print(inst.isPalindrome("A0 man, a plan, a canal: Panam0a"))