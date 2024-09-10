class Solution:
    def largestRect(self,heights):
        maxArea=0
        stack=[]
        
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                index,height=stack.pop()
                maxArea=max(maxArea,height*(i-index))
                start=i
                
            stack.append((start,h))
        for i,h in stack:
            maxArea=max(maxArea,h*(len(heights)-i))
        return maxArea
    
solution=Solution()
result=solution.largestRect([2,1,5,6,3,2])
print(result)