#two pointer, and find max throw array

def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxprofit = 0
        while right < len(prices):
            cur = prices[right] - prices[left]
            if prices[left]<prices[right]:
                maxprofit = max(maxprofit,cur)
            else:
                left = right
            right+=1
        return maxprofit
