class Solution:
    def maxProfit(self, prices):
        
        # sliding  window

        left = 0
        right = 1
        profit = 0
        
        while right < len(prices):
            
            profit = max(profit,(prices[right]-prices[left]))
            if prices[right]< prices[left]:
                left = right
            right +=1
        return profit
prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
obj = Solution()
print(obj.maxProfit(prices))