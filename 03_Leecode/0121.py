class Solution:
    def maxProfit_simple(self, prices: list[int]) -> int:
        """
        暴力解法， O(n^2)
        """
        cur_max_profit = 0
        n = len(prices)
        for i in range(0, n):
            for j in range(i, n):
                profit = prices[j] - prices[i]
                if cur_max_profit < profit:
                    cur_max_profit = profit
        return cur_max_profit

    def maxProfit(self, prices: list[int]) -> int:
        """
        最大利润的关键是两件事：
            记录到目前为止出现的最低价格
            记录 当前价格 - 最大价格能获得的最大利润
        """
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            cur_profit = price - min_price
            if cur_profit > max_profit:
                max_profit = cur_profit
        return max_profit


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0)
    ]
    for case in cases:
        r1 = solution.maxProfit_simple(case[0])
        r2 = solution.maxProfit(case[0])
        print(r1, r2, case[1])
