class TimeMap(object):

    def __init__(self):
        self.dic = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.dic[key].append([timestamp,value])
        
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        arr = self.dic[key]
        n=len(arr)
        l,r = 0,n
        while l<r:
            mid = (l+r)/2
            if arr[mid][0] <= timestamp:
                l = mid+1
            else:
                r=mid 
        return "" if r==0 else arr[r-1][1]
