# build dict to count and use heap to keep k numbers

def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 1:
            return [nums[0]]
        #build dict with cnt
        d={}
        for num in nums:
            d[num] = d.get(num,0)+1
        h=[]
        from heapq import heappush,heappop
        for key in d:
            heappush(h,(d[key], key))
            if len(h)>k:
                heappop(h)
        res = []
        while h:
            freq,item = heappop(h)
            res.append(item)
        return res
