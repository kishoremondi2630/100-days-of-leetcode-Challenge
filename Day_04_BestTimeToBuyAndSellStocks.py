class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0 #If its not prices

        min_price = prices[0]
        max_profit = 0 #Initial Assumption of Profit

        for price in prices[1:]:
            if price < min_price:
                min_price = price #Buying Price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit #Final Profit

        return max_profit
