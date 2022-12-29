class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        d={}
        l=[]
        for i in range(n):
            ntf= target-nums[i]
            if ntf in d.keys():
                l.append(d[ntf])
                l.append(i)

            d[nums[i]] = i
        return l 
