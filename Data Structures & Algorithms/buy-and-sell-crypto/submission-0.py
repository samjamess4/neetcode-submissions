class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left_index = 0
        right_index = 1
        max_profit = 0 
        
        while right_index < len(prices):

            if prices[left_index] < prices[right_index]:
                current_profit = prices[right_index] -  prices[left_index]
                max_profit = max(max_profit, current_profit)

            else: 
                left_index = right_index 
            
            right_index += 1
            

        return max_profit 



            
            




     

    
        
