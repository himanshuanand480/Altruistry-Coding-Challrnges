def max_profit_brute_force(prices):
    n = len(prices)
    max_profit = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    
    return max_profit
n = int(input().strip())
prices = [int(input().strip()) for _ in range(n)]
print(max_profit_brute_force(prices))

#Time complexity:O(N2)
#Space Complexity:O(1)
