class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # Sorting
        # prices.sort()
        
        # if (prices[0] + prices[1]) > money:
        #     return money
        
        # return money - (prices[0] + prices[1])

        # Greedy
        min1 = min2 = float("inf")

        for p in prices:
            if p < min1:
                min1, min2 = p, min1
            elif p < min2:
                min2 = p

        leftover = money - min1 - min2

        return leftover if leftover >= 0 else money