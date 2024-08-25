class Solution:
    def topKFrequent(self,nums,k):
        count={}
        freq=[[] for i in range(len(nums)+1)]
        print(freq)
        for n in nums:
            count[n]=1+count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
        

solution=Solution()
result=solution.topKFrequent([1,2,3,1],2)

print(result)