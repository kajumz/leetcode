def lengthOfLongestSubstring(self, s):
        l = 0
        ans = 0 
        used = {}
        for r in range(len(s)):
            if s[r] in used and l<=used[s[r]]:
                l=used[s[r]] + 1
            else:
                ans = max(ans,r-l+1)
            used[s[r]]=r
        return ans
