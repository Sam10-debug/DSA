class Solution:
    
    def TwoSumII(self,nums,target):
        l,r=0,len(nums)-1
        while l<r:
            currSum=nums[l]+nums[r]
            if currSum>target:
                r-=1
            elif currSum<target:
                l+=1
            else:
                return [l+1,r+1]
            
solution =Solution()
result=solution.TwoSumII([1,3,4,5,7,11],9)
print(result)