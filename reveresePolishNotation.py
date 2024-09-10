class Solution:
    def rPN(self,arr):
        res=[]
        for a in arr:
            if a=="+":
                res.append(res.pop()+res.pop())
            elif a=="*":
                res.append(res.pop()*res.pop())
            elif a=="-":
                c,b=res.pop(),res.pop()
                res.append(b-c)
            elif a=="/":
                c,b=res.pop(),res.pop()
                res.append(int(b/c))
            else:
                res.append(int(a))
        return res
    
solution=Solution()
result=solution.rPN(["2","1","-","3","/"])
print(result)