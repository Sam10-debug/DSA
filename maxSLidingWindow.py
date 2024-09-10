import collections

class Solution:
    def maxSlidingWindow(self,nums,k):
        output=[]
        l=r=0
        q=collections.deque()
        while r<len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            if l>q[0]:
                q.popleft()
            if (r+1)>=k:
                output.append(nums[q[-1]])
                l+=1
            r+=1
        return output

solution=Solution()
result=solution.maxSlidingWindow([1,1,1,1,1,4,5],6)
print(result)