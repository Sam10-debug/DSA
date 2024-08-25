from collections import defaultdict

class Solution:
    def group_anagram(self,strs):
        res=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                
                count[ord(c)-ord('a')]+=1
                
            res[tuple(count)].append(s)
        return res.values()
        

solution =Solution()
result=solution.group_anagram(['sam','mas','ate','tea','nat'])
print(result)