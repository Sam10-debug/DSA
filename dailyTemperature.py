class Solution:
    def dailyTemperature(self,temps):
        res=[0]*len(temps)
        stack=[]
        for i,t in enumerate(temps):
            while stack and t>stack[-1][0]:
                stackT,stackIndex=stack.pop()
                res[stackIndex]=(i-stackIndex)
            stack.append([t,i])
        return res

solution=Solution()
result=solution.dailyTemperature([73,74,75,71,69,72,76,63])
print(result)