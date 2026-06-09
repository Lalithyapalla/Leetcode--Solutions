class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        high = 0
        for i in range(len(accounts)):
            accounts[i] = sum(accounts[i])
            if high < accounts[i]:
                high = accounts[i]
        return high