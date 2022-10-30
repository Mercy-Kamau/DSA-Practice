# [4,3,2,1]
def maxProfit(prices):
    left_pointer = 0
    right_pointer = 1
    maxprofit = 0
    while right_pointer < len(prices)-1:
        profit = prices[right_pointer] - prices[left_pointer]
        if profit > 0:
            if profit > maxprofit:
                maxprofit = profit
            right_pointer = right_pointer + 1
        else:
            left_pointer = right_pointer
            right_pointer = right_pointer + 1
    return maxprofit