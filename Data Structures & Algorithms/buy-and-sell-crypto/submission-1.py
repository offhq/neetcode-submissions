class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left = 0
        right = 1
        max_p = 0
        if  n == 1:
            return max_p
        while right <= n - 1:
            p = prices[right] - prices[left]
            if p > max_p:
                max_p = p
            if prices[right] < prices[left]:
                left = right

            right += 1

        return max_p
            

        