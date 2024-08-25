class Solution:
    def trapWater(self,height):
        if not height:
            return 0
        l,r=0,len(height)-1
        leftMax,rightMax=height[l],height[r]
        res=0
        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax=max(height[l],leftMax)
                res+=leftMax-height[l]
            else:
                r-=1
                rightMax=max(height[r],rightMax)
                res+=rightMax-height[r]
        return res

solution =Solution()
result=solution.trapWater([0,1,0,2,1,0,1,3,2,1,2,1])
print(result)
    
