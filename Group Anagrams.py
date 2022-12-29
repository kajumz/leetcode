#for each word cnt char using number representation of char(ord)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            cnt = [0]*26
            for c in s:
                cnt[ord(c) - ord('a')]+=1
            ans[tuple(cnt)].append(s)
        return ans.values()
