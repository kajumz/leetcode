#use set and check prev num in this set, if not, so we can start our lcs with this num

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len=0
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                cur_num=num+1
                cur_len = 1
                while cur_num in nums:
                    cur_len+=1
                    cur_num+=1

                max_len = max(max_len,cur_len)
        return max_len
