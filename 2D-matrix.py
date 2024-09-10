#matrix=[[1,3,5], [7,9,13],[15,21,25]]

class Solution:
    def twoDMatrix(self,matrix,target):
        rows,cols= len(matrix), len(matrix[0])
        l,r=0,rows-1
        while l<=r:
            m=(l+r)//2
            if target>matrix[m][-1]:
                l=m+1
            elif target<matrix[m][0]:
                r=m-1
            else:
                break
            
        if not(l<=r):
            return False
        
        mid=(l+r)//2
        l1,r1=0,cols-1
        while l1<=r1:
            m=(l1+r1)//2
            if target>matrix[mid][m]:
                l1=m+1
            elif target<matrix[mid][m]:
                r1=m-1
            else:
                return True
        
        return False
    
solution=Solution()
result= solution.twoDMatrix([[1,3,5], [7,9,13],[15,21,25]],22)
print(result)