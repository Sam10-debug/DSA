class Solution:
    def carFleet(self,target,position,speed):
        stack=[]
        pair=[[p,s] for p,s in zip(position,speed) ]
        
        for x,y in sorted(pair)[::-1]:
            time= (target-x)/y
            stack.append(time)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        
        return len(stack)
    
solution=Solution()
result=solution.carFleet(10,[3,5,7],[3,2,1])
print(result)