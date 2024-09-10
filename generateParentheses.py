class Solution:
    def generateParentheses(self,n):
        stack=[]
        res=[]
        def backTrack(openN,closedN):
            if openN==closedN==n:
                res.append("".join(stack))
            if openN<n:
                stack.append("(")
                backTrack(openN+1,closedN)
                stack.pop()
            if closedN<openN:
                stack.append(")")
                backTrack(openN,closedN+1)
                stack.pop()
                
        backTrack(0,0)
        return res
    
solution=Solution()
res=solution.generateParentheses(3)
print(res)