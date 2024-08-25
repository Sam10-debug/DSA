class Solution:
    def twoSum(self,nums,target):
        prevMap={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n]=i
        return
    
solution=Solution()
result=solution.twoSum([1,7,3,4],11)
print(result)
