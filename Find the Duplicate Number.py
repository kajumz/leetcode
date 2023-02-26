def findDuplicate(self, nums: List[int]) -> int:
        a=set()
        for num in nums:
            if num in a:
                return num
            a.add(num)
        return -1
