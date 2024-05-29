from typing import List

class Solution:
    def containsDuplicate(self,nums:List[int])->bool:
        hashset=set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
    
solution = Solution()
result = solution.containsDuplicate([1, 2, 3, 4, 5])
print(result)

