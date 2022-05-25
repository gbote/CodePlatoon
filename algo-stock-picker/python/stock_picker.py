def picker(prices):
    max_profit = prices[1] - prices[0]
    min_index = 0
    buy_index = 0
    sell_index = 1

    for i in range(1, len(prices)):
        if prices[i] - prices[min_index] > max_profit:
            max_profit = prices[i] - prices[min_index]
            sell_index = i
            buy_index = min_index
        if prices[i] < prices[min_index]:      
            min_index = i

    return[buy_index, sell_index]