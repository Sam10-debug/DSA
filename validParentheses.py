class Solution:
    def validParentheses(self,str):
        #eg input="([])"
        stack=[]
        lol={")":"(","]":"[","}":"{"}
        for c in str:
            if c in lol:
                if stack and stack[-1]==lol[c]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(c)
        return True if not stack else False
    

solution=Solution()
result=solution.validParentheses("{()}]")
print(result)