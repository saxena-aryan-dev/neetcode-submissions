class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        maxi=0
        l=r=0
        charset=set()
        while r <n:

            while s[r]  in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            maxi=max(maxi,len(charset))
            r+=1
                
        return maxi            
                


           
            

        
        