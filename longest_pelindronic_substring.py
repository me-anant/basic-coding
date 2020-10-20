class Solution:
    def helper(self,a,i,j):
        t=0
        while(i>=0 and j<len(a)):
            if(a[i]==a[j]):
                i-=1
                j+=1
                t+=1
            else:
                break
        return t
    def longestPalindrome(self, s: str) -> str:
        ans=""
        for i in range(len(s)):
            t1,t2=self.helper(s,i-1,i),self.helper(s,i-1,i+1)
            if(len(ans)<2*t1>2*t2+1):
                ans=s[i-t1:i+t1]
            elif(len(ans)<2*t2+1>2*t1):
                ans=s[i-t2:i+t2+1]
        return ans
