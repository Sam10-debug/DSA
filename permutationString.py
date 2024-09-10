class Solution:
    def permutation(self,s1,s2):
        if len(s1)>len(s2):
            return False
        s1count,s2count=[0]*26,[0]*26
        for i in range(len(s1)):
            s1count[ord(s1[i])-ord('a')]+=1
            s2count[ord(s2[i])-ord('a')]+=1
        matches=0
        for i in range(26):
            matches+=(1 if s1count[i]==s2count[i] else 0)
        l=0
        for r in range(len(s1),len(s2)):
            if matches==26:
                return True
            index=ord(s2[r])-ord('a')
            s2count[index]+=1
            if s1count[index]==s2count[index]:
                matches+=1
            elif s1count[index]+1==s2count[index]:
                matches-=1
            index=ord(s2[l])-ord('a')
            s2count[index]-=1
            if s1count[index]==s2count[index]:
                matches+=1
            elif s1count[index]-1==s2count[index]:
                matches-=1
            l+=1
        return matches==26
    
# solution=Solution()
# result=solution.permutation("abc","baxyzabc")
# print(result)

#MY APPROACH USING HASHMAP

class Solution1:
    def permutation(self,s1,s2):
        if len(s1)>len(s2):
            return False
        s1count,s2count={},{}
        for i in range(26):
            s1count[i]=0
            s2count[i]=0
        for i in range(len(s1)):
            s1count[ord(s1[i])-ord('a')]+=1
            s2count[ord(s2[i])-ord('a')]+=1
        matches=0
        for i in range(26):
            matches+=(1 if s1count[i]==s2count[i] else 0)
        l=0
        for r in range(len(s1),len(s2)):
            if matches==26:
                return True
            s2count[ord(s2[r])-ord('a')]+=1
            if s1count[ord(s2[r])-ord('a')]==s2count[ord(s2[r])-ord('a')]:
                matches+=1
            elif s1count[ord(s2[r])-ord('a')]+1==s2count[ord(s2[r])-ord('a')]:
                matches-=1
           
            s2count[ord(s2[l])-ord('a')]+=1
            if s1count[ord(s2[r])-ord('a')]==s2count[ord(s2[r])-ord('a')]:
                matches+=1
            elif s1count[ord(s2[r])-ord('a')]-1==s2count[ord(s2[r])-ord('a')]:
                matches-=1
            
            l+=1
        return matches==26

solution1=Solution()
result1=solution1.permutation("abc","bacxyzab")
print(result1)