#There are two solutions to this

# class Solution:
#     def isPalindrome(self,s):
#         newStr=""
#         for c in s:
#             if c.isalnum():
#                 newStr+=c.lower()
#         return newStr==newStr[::-1]
    
# solution=Solution()
# result= solution.isPalindrome("ab a")
# print(result)

#second solution
class Solution:
    
    def alphaNum(self,c):
        return (ord('A')<=ord(c)<=ord('Z') or ord('a')<=ord(c)<=ord('z') or ord('0')<=ord(c)<=ord('9')) 
    
    def isPalindrome(self,s):
        l,r=0,len(s)-1
        while l<r and not self.alphaNum(s[l]):
            l+=1
        while r>l and not self.alphaNum(s[r]):
            r-=1
        if s[l].lower()!=s[r].lower():
            return False
        l,r=l+1,r-1
        return True

    
solution=Solution()
result= solution.isPalindrome("ab a")
print(result)